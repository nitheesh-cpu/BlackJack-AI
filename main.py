import shutil
import os
import base64
import uuid
import csv

import flask
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask import send_file
from flask import jsonify
from flask import json

from py4web.core import wsgi

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont




model = YOLO("model.pt")
# model.predict(source="2", show=True, conf=0.2)

# Q: How do I see the x and y coordinates of the bounding boxes?
# A:
names = ['10C', '10D', '10H', '10S', '2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S', '4C', '4D', '4H', '4S', '5C', '5D', '5H', '5S', '6C', '6D', '6H', '6S', '7C',
         '7D', '7H', '7S', '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S', 'AC', 'AD', 'AH', 'AS', 'JC', 'JD', 'JH', 'JS', 'KC', 'KD', 'KH', 'KS', 'QC', 'QD', 'QH', 'QS']

app = flask.Flask(__name__, template_folder='templates')


def predict(image):
    print(image)
    img = Image.open(image)
    results = model.predict(img, conf=0.45, save=True, show_conf=False, imgsz=615)
    height = results[0].orig_shape[0]

    dealer_hand = []
    player_hand = []

    boxes = results[0].boxes
    for box in boxes:
        if box.xywh.int().numpy().tolist()[0][1] < height/2 and names[int(box.cls.item())] not in dealer_hand:
            dealer_hand.append(names[int(box.cls.item())])
            
        elif box.xywh.int().numpy().tolist()[0][1] > height/2 and names[int(box.cls.item())] not in player_hand:
            player_hand.append(names[int(box.cls.item())])

    # remove the suits from the cards
    dealer_hand = [i[:-1] for i in dealer_hand]
    player_hand = [i[:-1] for i in player_hand]

    #player hand is the larger hand (bottom half)
    if len(player_hand) < len(dealer_hand):
        temp = player_hand
        player_hand = dealer_hand
        dealer_hand = temp

    if(len(dealer_hand) == 0):
        print("No cards found in the top half!")
    if(len(player_hand) == 0):
        print("No cards found in the bottom half!")

    deck = ['A', 'A', 'A', 'A', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', 
            '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']

    for card in dealer_hand:
        deck.remove(card)
    for card in player_hand:
        deck.remove(card)

    dealer_value = 0
    player_value = 0

    print("Dealer hand: " + str(dealer_hand))
    print("Player hand: " + str(player_hand))

    def card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)

    for card in dealer_hand:
        dealer_value += card_value(card)
    for card in player_hand:
        player_value += card_value(card)

    print("Dealer value: " + str(dealer_value))
    print("Player value: " + str(player_value))

    decision = ""
    percent = 0

    if(player_value == 21):
        decision = "Blackjack!"
        percent = 100

    # check strategy.csv for decision
    # if player has an ace, check if it's soft or hard

    hard = False
    for card in player_hand:
            if card == 'A':
                hard = False
    
    # open csv file

    with open('strategy.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        # find the row that matches the player's hand
        for row in reader:
            if row[0] == str(player_value) and row[1] == str(dealer_value) and row[2].lower() == str(hard).lower():
                decision = row[3]
                percent = 100
                break

    # if('A' in player_hand):
    #     if(player_value >= 19):
    #         decision = "Stand"
    #         percent = 100
    #     elif(player_value == 18 and dealer_value < 9):
    #         decision = "Stand"
    #         percent = 100
    #     elif(player_value == 18 and dealer_value >= 9):
    #         decision = "Hit"
    #         percent = 100
    #     else:
    #         decision = "Hit"
    #         percent = 100

    # else:
    #     if(player_value > 11 and player_value < 17 and dealer_value >= 10):
    #         # determine percentage of next card not busting
    #         percent = 0
    #         for card in deck:
    #             if player_value + card_value(card) <= 21:
    #                 percent += 1
    #         percent = percent / len(deck) * 100
    #         percent = round(percent)
    #         if percent > 50:
    #             decision = "Hit"
    #         else:
    #             decision = "Stand"
    #             percent = 100 - percent
        
    #     if(player_value >= 17):
    #         decision = "Stand"
    #         percent = 100

    #     if(player_value <= 11):
    #         decision = "Hit"
    #         percent = 100

    # move predict/image0.jpg to IMG_2306.jpg

    directory = 'runs/detect'
    files = os.listdir(directory)
    shutil.rmtree(r"runs")

    img = Image.open(image)
    font = ImageFont.truetype("OpenSans-Semibold.ttf", 60)
    font2 = ImageFont.truetype("OpenSans-Semibold.ttf", 30)
    draw = ImageDraw.Draw(img)
    draw.text((10, 0), "Dealer Value: " + str(dealer_value), font=font2, fill=(0, 255, 255))
    draw.text((10, 270), "Player Value: " + str(player_value), font=font2, fill=(0, 255, 255))
    decision = decision.capitalize()
    if(decision == "Hit"):
        draw.text((10, 530), decision + " (" + str(percent) + "%)", font=font, fill=(255, 0, 0))
    else:
        draw.text((10, 530), decision + " (" + str(percent) + "%)", font=font, fill=(0, 255, 0))
    clone = img.copy()
    # save image to browser

    clone.save("predicted.jpg")
    img.close()

    return clone


@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    name = uuid.uuid4().hex

    if flask.request.method == 'POST':
        # reverse base64 encoding and save to file
        image_b64 = flask.request.values['image']
        # cast to bASE64
        image_b64 = image_b64.split(',')[1]
        # decode
        image_data = bytes(image_b64, encoding="ascii")
        file_name = name + ".png"

        with open(file_name, "wb") as fh:
            fh.write(base64.decodebytes(image_data))

    # Predict
    img = predict(file_name)


    # Save to new file
    img.save("images/" + str(name) + ".jpg")

    # remove old file
    os.remove(file_name)


    # return image url
    return flask.jsonify({'image_url': str(name) + ".jpg"})

@app.route('/predicted.jpg')
def predicted():
    return flask.send_file("predicted.jpg", mimetype='image/gif')

@app.route('/imageToSave.png')
def imageToSave():
    return flask.send_file("imageToSave.png", mimetype='image/gif')

@app.route('/image')
def image():
    image_url = flask.request.args.get('image_url')
    image_url = "images/" + image_url
    # find image in images folder
    return flask.send_file(image_url, mimetype='image/gif')



@app.route('/result')
def result():
    return flask.render_template('results.html')



@app.route('/help')
def help():
    return flask.render_template('help.html')


app.run(host='localhost', port=5000, debug=True)
