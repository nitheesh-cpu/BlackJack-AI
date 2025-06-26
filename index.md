---
layout: home
title: BlackJack AI - Computer Vision-Powered Strategy Advisor
---

# BlackJack AI

### Computer Vision-Powered Blackjack Strategy Advisor

<div class="text-center mb-12">
  <img src="{{ '/assets/img/blackjack-ai-demo.gif' | relative_url }}" alt="BlackJack AI Demo" class="mx-auto rounded-lg shadow-2xl border border-nord-3 max-w-4xl w-full">
</div>

## About

BlackJack AI is an intelligent web application that combines **computer vision** and **optimal blackjack strategy** to provide real-time decision-making assistance. Simply upload an image of your blackjack hand, and the AI will analyze the cards using YOLO object detection, calculate hand values, and recommend the statistically optimal move based on professional blackjack strategy.

---

## Features {#features}

<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
  <div class="bg-nord-1 p-6 rounded-lg border border-nord-3">
    <h3 class="text-blackjack-green text-xl font-bold mb-3">🎯 Real-time Card Detection</h3>
    <p class="text-nord-4">Advanced YOLO object detection identifies playing cards in uploaded images with high accuracy</p>
  </div>
  
  <div class="bg-nord-1 p-6 rounded-lg border border-nord-3">
    <h3 class="text-blackjack-green text-xl font-bold mb-3">🧠 Optimal Strategy Engine</h3>
    <p class="text-nord-4">Implements mathematically proven blackjack basic strategy for maximum winning probability</p>
  </div>
  
  <div class="bg-nord-1 p-6 rounded-lg border border-nord-3">
    <h3 class="text-blackjack-green text-xl font-bold mb-3">💻 Web-based Interface</h3>
    <p class="text-nord-4">Clean, responsive Flask web application with intuitive drag-and-drop image upload</p>
  </div>
  
  <div class="bg-nord-1 p-6 rounded-lg border border-nord-3">
    <h3 class="text-blackjack-green text-xl font-bold mb-3">📊 Visual Feedback</h3>
    <p class="text-nord-4">Annotated images showing detected cards, hand values, and strategy recommendations</p>
  </div>
  
  <div class="bg-nord-1 p-6 rounded-lg border border-nord-3">
    <h3 class="text-blackjack-green text-xl font-bold mb-3">⚡ Fast Processing</h3>
    <p class="text-nord-4">Optimized YOLO model provides near-instant card recognition and strategy calculation</p>
  </div>
  
  <div class="bg-nord-1 p-6 rounded-lg border border-nord-3">
    <h3 class="text-blackjack-green text-xl font-bold mb-3">🎨 Modern UI/UX</h3>
    <p class="text-nord-4">Dark theme with matrix-style animations creating an engaging user experience</p>
  </div>
</div>

---

## How It Works {#how-it-works}

<div class="bg-nord-1 p-8 rounded-lg border border-nord-3 mb-8">
  <div class="grid md:grid-cols-2 gap-8 items-center">
    <div>
      <h3 class="text-2xl font-bold text-blackjack-green mb-4">1. Upload Your Hand</h3>
      <p class="text-nord-4 mb-4">Take a photo of your blackjack table or upload an existing image. The application accepts various image formats and automatically resizes for optimal processing.</p>
      
      <h3 class="text-2xl font-bold text-blackjack-green mb-4">2. AI Card Detection</h3>
      <p class="text-nord-4 mb-4">Our trained YOLO model detects and identifies all visible playing cards, distinguishing between dealer and player hands based on position.</p>
      
      <h3 class="text-2xl font-bold text-blackjack-green mb-4">3. Strategy Calculation</h3>
      <p class="text-nord-4">The system calculates hand values, considers soft/hard aces, and references the optimal basic strategy table to provide the best statistical move.</p>
    </div>
    <div class="text-center">
      <img src="{{ '/assets/img/card-detection-example.png' | relative_url }}" alt="Card Detection Example" class="rounded-lg shadow-lg border border-nord-3 w-full max-w-md">
    </div>
  </div>
</div>

### Strategy Recommendations

<div class="grid md:grid-cols-3 gap-6 mb-8">
  <div class="bg-nord-2 p-6 rounded-lg text-center">
    <div class="text-3xl mb-2">✊</div>
    <h4 class="text-xl font-bold text-nord-6 mb-2">Stand</h4>
    <p class="text-nord-4 text-sm">Keep your current hand - optimal when risk of busting is too high</p>
  </div>
  
  <div class="bg-nord-2 p-6 rounded-lg text-center">
    <div class="text-3xl mb-2">👆</div>
    <h4 class="text-xl font-bold text-nord-6 mb-2">Hit</h4>
    <p class="text-nord-4 text-sm">Take another card - when probability favors improving your hand</p>
  </div>
  
  <div class="bg-nord-2 p-6 rounded-lg text-center">
    <div class="text-3xl mb-2">⏫</div>
    <h4 class="text-xl font-bold text-nord-6 mb-2">Double</h4>
    <p class="text-nord-4 text-sm">Double your bet and take exactly one more card - maximum advantage scenarios</p>
  </div>
</div>

### Example Output

<div class="text-center mb-8">
  <img src="{{ '/assets/img/strategy-recommendation.jpg' | relative_url }}" alt="Strategy Recommendation Output" class="mx-auto rounded-lg shadow-lg border border-nord-3 max-w-2xl w-full">
  <p class="text-nord-4 text-sm mt-4">Example output showing detected cards, calculated values, and optimal strategy recommendation</p>
</div>

---

## Technology Stack {#technology}

<div class="grid md:grid-cols-2 gap-8 mb-8">
  <div class="bg-nord-1 p-6 rounded-lg border border-nord-3">
    <h3 class="text-xl font-bold text-blackjack-green mb-4">🤖 Machine Learning</h3>
    <div class="space-y-2 text-nord-4">
      <div class="flex items-center space-x-2">
        <span class="w-2 h-2 bg-blackjack-green rounded-full"></span>
        <span><strong>YOLO (You Only Look Once):</strong> Real-time object detection</span>
      </div>
      <div class="flex items-center space-x-2">
        <span class="w-2 h-2 bg-blackjack-green rounded-full"></span>
        <span><strong>Ultralytics:</strong> Modern YOLO implementation</span>
      </div>
      <div class="flex items-center space-x-2">
        <span class="w-2 h-2 bg-blackjack-green rounded-full"></span>
        <span><strong>Custom Training:</strong> 52-card deck recognition</span>
      </div>
    </div>
  </div>
  
  <div class="bg-nord-1 p-6 rounded-lg border border-nord-3">
    <h3 class="text-xl font-bold text-blackjack-green mb-4">🌐 Web Framework</h3>
    <div class="space-y-2 text-nord-4">
      <div class="flex items-center space-x-2">
        <span class="w-2 h-2 bg-blackjack-green rounded-full"></span>
        <span><strong>Flask:</strong> Lightweight Python web framework</span>
      </div>
      <div class="flex items-center space-x-2">
        <span class="w-2 h-2 bg-blackjack-green rounded-full"></span>
        <span><strong>JavaScript/jQuery:</strong> Interactive frontend</span>
      </div>
      <div class="flex items-center space-x-2">
        <span class="w-2 h-2 bg-blackjack-green rounded-full"></span>
        <span><strong>Tailwind CSS:</strong> Modern responsive styling</span>
      </div>
    </div>
  </div>
  
  <div class="bg-nord-1 p-6 rounded-lg border border-nord-3">
    <h3 class="text-xl font-bold text-blackjack-green mb-4">🖼️ Image Processing</h3>
    <div class="space-y-2 text-nord-4">
      <div class="flex items-center space-x-2">
        <span class="w-2 h-2 bg-blackjack-green rounded-full"></span>
        <span><strong>PIL (Pillow):</strong> Image manipulation and annotation</span>
      </div>
      <div class="flex items-center space-x-2">
        <span class="w-2 h-2 bg-blackjack-green rounded-full"></span>
        <span><strong>OpenCV:</strong> Computer vision operations</span>
      </div>
      <div class="flex items-center space-x-2">
        <span class="w-2 h-2 bg-blackjack-green rounded-full"></span>
        <span><strong>Base64 Encoding:</strong> Web-optimized image transfer</span>
      </div>
    </div>
  </div>
  
  <div class="bg-nord-1 p-6 rounded-lg border border-nord-3">
    <h3 class="text-xl font-bold text-blackjack-green mb-4">📈 Strategy Engine</h3>
    <div class="space-y-2 text-nord-4">
      <div class="flex items-center space-x-2">
        <span class="w-2 h-2 bg-blackjack-green rounded-full"></span>
        <span><strong>CSV Database:</strong> Comprehensive strategy lookup table</span>
      </div>
      <div class="flex items-center space-x-2">
        <span class="w-2 h-2 bg-blackjack-green rounded-full"></span>
        <span><strong>Basic Strategy:</strong> Mathematically optimal decisions</span>
      </div>
      <div class="flex items-center space-x-2">
        <span class="w-2 h-2 bg-blackjack-green rounded-full"></span>
        <span><strong>Soft/Hard Ace Logic:</strong> Advanced hand evaluation</span>
      </div>
    </div>
  </div>
</div>

---

## Key Features Breakdown

<div class="space-y-6 mb-8">
  <div class="bg-nord-1 p-6 rounded-lg border border-nord-3">
    <h3 class="text-xl font-bold text-blackjack-green mb-3">🎯 Card Recognition Accuracy</h3>
    <p class="text-nord-4 mb-3">The YOLO model is trained to recognize all 52 playing cards with suit and rank detection:</p>
    <div class="bg-nord-2 p-4 rounded font-mono text-sm">
      <div class="grid grid-cols-4 gap-2 text-center">
        <div class="text-red-400">♥ Hearts: A, 2-10, J, Q, K</div>
        <div class="text-red-400">♦ Diamonds: A, 2-10, J, Q, K</div>
        <div class="text-nord-6">♠ Spades: A, 2-10, J, Q, K</div>
        <div class="text-nord-6">♣ Clubs: A, 2-10, J, Q, K</div>
      </div>
    </div>
  </div>
  
  <div class="bg-nord-1 p-6 rounded-lg border border-nord-3">
    <h3 class="text-xl font-bold text-blackjack-green mb-3">📊 Strategy Database</h3>
    <p class="text-nord-4 mb-3">Comprehensive lookup table covering all possible game scenarios:</p>
    <ul class="list-disc list-inside text-nord-4 space-y-1">
      <li>Hard hands (no ace or ace counted as 1)</li>
      <li>Soft hands (ace counted as 11)</li>
      <li>All dealer up-cards (2-11)</li>
      <li>Split recommendations for pairs</li>
      <li>Double down opportunities</li>
    </ul>
  </div>
</div>

---

## Installation & Setup {#installation}

<div class="bg-nord-1 p-6 rounded-lg border border-nord-3 mb-8">
  <h3 class="text-xl font-bold text-blackjack-green mb-4">🚀 Quick Start</h3>
  
  <div class="space-y-4">
    <div>
      <h4 class="font-bold text-nord-6 mb-2">1. Clone the Repository</h4>
      <div class="bg-nord-2 p-3 rounded font-mono text-sm">
        <span class="text-blackjack-green">git clone</span> <span class="text-nord-4">https://github.com/username/BlackJack-AI.git</span><br>
        <span class="text-blackjack-green">cd</span> <span class="text-nord-4">BlackJack-AI</span>
      </div>
    </div>
    
    <div>
      <h4 class="font-bold text-nord-6 mb-2">2. Install Dependencies</h4>
      <div class="bg-nord-2 p-3 rounded font-mono text-sm">
        <span class="text-blackjack-green">pip install</span> <span class="text-nord-4">-r requirements.txt</span>
      </div>
    </div>
    
    <div>
      <h4 class="font-bold text-nord-6 mb-2">3. Run the Application</h4>
      <div class="bg-nord-2 p-3 rounded font-mono text-sm">
        <span class="text-blackjack-green">python</span> <span class="text-nord-4">main.py</span>
      </div>
    </div>
    
    <div>
      <h4 class="font-bold text-nord-6 mb-2">4. Access the Web Interface</h4>
      <div class="bg-nord-2 p-3 rounded font-mono text-sm">
        <span class="text-nord-4">Open browser to: </span><span class="text-blackjack-green">http://localhost:5000</span>
      </div>
    </div>
  </div>
</div>

### Requirements

<div class="grid md:grid-cols-2 gap-6 mb-8">
  <div class="bg-nord-1 p-6 rounded-lg border border-nord-3">
    <h4 class="font-bold text-blackjack-green mb-3">📦 Python Dependencies</h4>
    <ul class="text-nord-4 space-y-1 font-mono text-sm">
      <li>• Flask - Web framework</li>
      <li>• ultralytics - YOLO implementation</li>
      <li>• Pillow - Image processing</li>
      <li>• opencv-python-headless - Computer vision</li>
      <li>• psutil - System monitoring</li>
      <li>• py4web - Additional web utilities</li>
    </ul>
  </div>
  
  <div class="bg-nord-1 p-6 rounded-lg border border-nord-3">
    <h4 class="font-bold text-blackjack-green mb-3">💻 System Requirements</h4>
    <ul class="text-nord-4 space-y-1">
      <li>• Python 3.8 or higher</li>
      <li>• 4GB RAM minimum</li>
      <li>• 500MB disk space</li>
      <li>• GPU optional (CPU inference supported)</li>
      <li>• Modern web browser</li>
    </ul>
  </div>
</div>

---

## Usage Examples

<div class="bg-nord-1 p-6 rounded-lg border border-nord-3 mb-8">
  <h3 class="text-xl font-bold text-blackjack-green mb-4">📸 Best Practices for Card Images</h3>
  <div class="grid md:grid-cols-2 gap-6">
    <div>
      <h4 class="font-bold text-nord-6 mb-2">✅ Good Images:</h4>
      <ul class="text-nord-4 space-y-1">
        <li>• Clear lighting, minimal shadows</li>
        <li>• Cards fully visible and unobstructed</li>
        <li>• Dealer hand in upper half of image</li>
        <li>• Player hand in lower half of image</li>
        <li>• Stable camera angle</li>
      </ul>
    </div>
    <div>
      <h4 class="font-bold text-nord-6 mb-2">❌ Avoid:</h4>
      <ul class="text-nord-4 space-y-1">
        <li>• Blurry or out-of-focus cards</li>
        <li>• Overlapping or obscured cards</li>
        <li>• Poor lighting conditions</li>
        <li>• Extreme angles or perspective</li>
        <li>• Reflective surfaces causing glare</li>
      </ul>
    </div>
  </div>
</div>

---

## Deployment Options

<div class="grid md:grid-cols-3 gap-6 mb-8">
  <div class="bg-nord-1 p-6 rounded-lg border border-nord-3 text-center">
    <h4 class="font-bold text-blackjack-green mb-3">🐳 Docker</h4>
    <p class="text-nord-4 text-sm">Containerized deployment with included Dockerfile for easy scaling</p>
  </div>
  
  <div class="bg-nord-1 p-6 rounded-lg border border-nord-3 text-center">
    <h4 class="font-bold text-blackjack-green mb-3">🚀 Heroku</h4>
    <p class="text-nord-4 text-sm">Cloud deployment ready with Procfile and heroku.yml configuration</p>
  </div>
  
  <div class="bg-nord-1 p-6 rounded-lg border border-nord-3 text-center">
    <h4 class="font-bold text-blackjack-green mb-3">⚡ Vercel</h4>
    <p class="text-nord-4 text-sm">Serverless deployment option with included vercel.json configuration</p>
  </div>
</div>

---

<div class="text-center bg-nord-1 p-8 rounded-lg border border-nord-3">
  <h2 class="text-2xl font-bold text-blackjack-green mb-4">Ready to Improve Your Blackjack Game?</h2>
  <p class="text-nord-4 mb-6">Upload an image of your blackjack hand and let AI guide your strategy decisions</p>
  <a href="#" class="inline-block bg-blackjack-green text-nord-0 px-8 py-3 rounded-lg font-bold hover:bg-nord-7 transition-colors">
    Try BlackJack AI Now
  </a>
</div>
