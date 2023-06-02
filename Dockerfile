FROM python:3.11-alpine
COPY . /app
RUN mkdir /app/images
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]
