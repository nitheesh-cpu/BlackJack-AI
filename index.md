---
layout: home
title: "BlackJack AI Project"
heading: "BlackJack AI"
subheading: "Computer Vision-Powered Blackjack Strategy Advisor using YOLO object detection"
---

<div class="space-y-12">
    <!-- Main Featured Image - Smaller and Centered -->
    <div class="flex justify-center">
        <img class="object-cover object-top w-full max-w-md h-auto rounded-lg shadow-lg" 
             src="{{ site.baseurl }}/assets/img/blackjack-ai-demo.gif" 
             alt="BlackJack AI Demo - Card Detection and Strategy">
    </div>

    <div class="space-y-6">
        <div class="space-y-4">
            <h3 class="text-3xl font-bold leading-tight text-gray-900 sm:text-4xl dark:text-white">
                Computer Vision-Powered Blackjack Strategy
            </h3>

            <p class="text-base font-normal text-gray-500 sm:text-lg dark:text-gray-400">
                BlackJack AI is an intelligent web application that combines <strong>computer vision</strong> and <strong>optimal blackjack strategy</strong> to provide real-time decision-making assistance. Simply upload an image of your blackjack hand, and the AI will analyze the cards using YOLO object detection, calculate hand values, and recommend the statistically optimal move based on professional blackjack strategy.
            </p>
            <p class="text-base font-normal text-gray-500 sm:text-lg dark:text-gray-400">
                The system uses a trained <a href="https://ultralytics.com/yolo" target="_blank" class="text-primary-600 hover:text-primary-700 dark:text-primary-500">YOLO model</a> to detect and identify all 52 playing cards, implements mathematically proven basic strategy, and provides instant recommendations with confidence percentages through a modern Flask web interface.
            </p>
        </div>

        <!-- Technology Tags -->
        <div class="flex items-center gap-2.5 flex-wrap">
            <div class="p-1 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800">
                <span class="inline-flex items-center px-3 py-1 text-xs font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300">
                    YOLO Object Detection
                </span>
            </div>
            <div class="p-1 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800">
                <span class="inline-flex items-center px-3 py-1 text-xs font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300">
                    Flask
                </span>
            </div>
            <div class="p-1 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800">
                <span class="inline-flex items-center px-3 py-1 text-xs font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300">
                    Computer Vision
                </span>
            </div>
            <div class="p-1 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800">
                <span class="inline-flex items-center px-3 py-1 text-xs font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300">
                    Machine Learning
                </span>
            </div>
            <div class="p-1 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800">
                <span class="inline-flex items-center px-3 py-1 text-xs font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300">
                    Basic Strategy
                </span>
            </div>
            <div class="p-1 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800">
                <span class="inline-flex items-center px-3 py-1 text-xs font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300">
                    Tailwind CSS
                </span>
            </div>
        </div>

        <!-- How It Works Section -->
        <div class="mt-8">
            <h4 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">How It Works</h4>
            <p class="text-base text-gray-500 dark:text-gray-400 mb-8">
                Upload an image of your blackjack table and get instant strategy recommendations:
            </p>

            <!-- Process Steps Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Upload Step -->
                <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-6">
                    <h5 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">1. Upload Your Hand</h5>
                    <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Take a photo of your blackjack table or upload an existing image. The application accepts various image formats and automatically resizes for optimal processing.</p>
                    <img class="w-full h-auto rounded border border-gray-200 dark:border-gray-700"
                         src="{{ site.baseurl }}/assets/img/card-detection-example.png" alt="Card Detection Input">
                </div>

                <!-- AI Detection Step -->
                <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-6">
                    <h5 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">2. AI Card Detection</h5>
                    <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Our trained YOLO model detects and identifies all visible playing cards, distinguishing between dealer and player hands based on position.</p>
                    <img class="w-full h-auto rounded border border-gray-200 dark:border-gray-700"
                         src="{{ site.baseurl }}/assets/img/strategy-recommendation.jpg" alt="Strategy Output">
                </div>

                <!-- Strategy Calculation -->
                <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-6 md:col-span-2">
                    <h5 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">3. Strategy Calculation</h5>
                    <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">The system calculates hand values, considers soft/hard aces, and references the optimal basic strategy table to provide the best statistical move with confidence percentage.</p>

                    <!-- Strategy Recommendations -->
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-4">
                        <div class="bg-white dark:bg-gray-800 p-4 rounded-lg text-center border border-gray-200 dark:border-gray-600">
                            <div class="text-2xl mb-2">✊</div>
                            <h6 class="font-bold text-gray-900 dark:text-white">Stand</h6>
                            <p class="text-xs text-gray-600 dark:text-gray-400">Keep current hand</p>
                        </div>
                        <div class="bg-white dark:bg-gray-800 p-4 rounded-lg text-center border border-gray-200 dark:border-gray-600">
                            <div class="text-2xl mb-2">👆</div>
                            <h6 class="font-bold text-gray-900 dark:text-white">Hit</h6>
                            <p class="text-xs text-gray-600 dark:text-gray-400">Take another card</p>
                        </div>
                        <div class="bg-white dark:bg-gray-800 p-4 rounded-lg text-center border border-gray-200 dark:border-gray-600">
                            <div class="text-2xl mb-2">⏫</div>
                            <h6 class="font-bold text-gray-900 dark:text-white">Double</h6>
                            <p class="text-xs text-gray-600 dark:text-gray-400">Double bet, one card</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Key Features Section -->
        <div class="mt-8">
            <h4 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">Key Features</h4>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-6">
                    <div class="text-2xl mb-3">🎯</div>
                    <h5 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">Real-time Card Detection</h5>
                    <p class="text-sm text-gray-600 dark:text-gray-400">Advanced YOLO object detection identifies playing cards in uploaded images with high accuracy across all 52 cards.</p>
                </div>

                <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-6">
                    <div class="text-2xl mb-3">🧠</div>
                    <h5 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">Optimal Strategy Engine</h5>
                    <p class="text-sm text-gray-600 dark:text-gray-400">Implements mathematically proven blackjack basic strategy for maximum winning probability.</p>
                </div>

                <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-6">
                    <div class="text-2xl mb-3">💻</div>
                    <h5 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">Web-based Interface</h5>
                    <p class="text-sm text-gray-600 dark:text-gray-400">Clean, responsive Flask web application with intuitive drag-and-drop image upload.</p>
                </div>

                <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-6">
                    <div class="text-2xl mb-3">📊</div>
                    <h5 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">Visual Feedback</h5>
                    <p class="text-sm text-gray-600 dark:text-gray-400">Annotated images showing detected cards, hand values, and strategy recommendations.</p>
                </div>

                <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-6">
                    <div class="text-2xl mb-3">⚡</div>
                    <h5 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">Fast Processing</h5>
                    <p class="text-sm text-gray-600 dark:text-gray-400">Optimized YOLO model provides near-instant card recognition and strategy calculation.</p>
                </div>

                <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-6">
                    <div class="text-2xl mb-3">🎨</div>
                    <h5 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">Modern UI/UX</h5>
                    <p class="text-sm text-gray-600 dark:text-gray-400">Dark theme with matrix-style animations creating an engaging user experience.</p>
                </div>
            </div>
        </div>

        <!-- Technical Implementation -->
        <div class="mt-8">
            <h4 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">Technical Implementation</h4>

            <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-6">
                <div class="grid md:grid-cols-2 gap-6">
                    <div>
                        <h5 class="text-lg font-semibold text-gray-900 dark:text-white mb-3">🤖 Machine Learning Stack</h5>
                        <ul class="text-sm text-gray-600 dark:text-gray-400 space-y-1">
                            <li>• <strong>YOLO (You Only Look Once):</strong> Real-time object detection</li>
                            <li>• <strong>Ultralytics:</strong> Modern YOLO implementation</li>
                            <li>• <strong>Custom Training:</strong> 52-card deck recognition</li>
                            <li>• <strong>PIL/Pillow:</strong> Image manipulation and annotation</li>
                        </ul>
                    </div>
                    <div>
                        <h5 class="text-lg font-semibold text-gray-900 dark:text-white mb-3">🌐 Web Framework</h5>
                        <ul class="text-sm text-gray-600 dark:text-gray-400 space-y-1">
                            <li>• <strong>Flask:</strong> Lightweight Python web framework</li>
                            <li>• <strong>JavaScript/jQuery:</strong> Interactive frontend</li>
                            <li>• <strong>Tailwind CSS:</strong> Modern responsive styling</li>
                            <li>• <strong>Base64 Encoding:</strong> Web-optimized image transfer</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- Installation Section -->
        <div class="mt-8">
            <h4 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">Quick Start</h4>

            <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-6">
                <div class="space-y-4">
                    <div>
                        <h5 class="font-bold text-gray-900 dark:text-white mb-2">1. Clone the Repository</h5>
                        <div class="bg-gray-800 text-gray-100 p-3 rounded font-mono text-sm">
                            git clone https://github.com/nitheesh-cpu/BlackJack-AI.git<br>
                            cd BlackJack-AI
                        </div>
                    </div>

                    <div>
                        <h5 class="font-bold text-gray-900 dark:text-white mb-2">2. Install Dependencies</h5>
                        <div class="bg-gray-800 text-gray-100 p-3 rounded font-mono text-sm">
                            pip install -r requirements.txt
                        </div>
                    </div>

                    <div>
                        <h5 class="font-bold text-gray-900 dark:text-white mb-2">3. Run the Application</h5>
                        <div class="bg-gray-800 text-gray-100 p-3 rounded font-mono text-sm">
                            python main.py
                        </div>
                    </div>

                    <div>
                        <h5 class="font-bold text-gray-900 dark:text-white mb-2">4. Access the Web Interface</h5>
                        <div class="bg-gray-800 text-gray-100 p-3 rounded font-mono text-sm">
                            Open browser to: http://localhost:5000
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- GitHub Button -->
        <div class="mt-8">
            <a href="https://github.com/nitheesh-cpu/BlackJack-AI" target="_blank" title="View on GitHub"
                class="text-white inline-flex items-center bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
                role="button">
                View Source Code
                <svg aria-hidden="true" class="w-5 h-5 ml-2" fill="none" stroke="currentColor"
                    stroke-width="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3">
                    </path>
                </svg>
            </a>
        </div>
    </div>

</div>
