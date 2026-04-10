# Hand-Gestures
A computer vision project that detects and interprets hand gestures in real-time using machine learning techniques. This system enables touchless interaction and can be applied in human-computer interaction, gaming, and accessibility solutions. works like Virtual Mouse And playing Games..


# 📌 🖐️ Hand Gesture Recognition System 

## 🧠 Project Overview

This project is a **real-time Hand Gesture Recognition System** that uses a webcam to detect and track hand movements. It can identify hand landmarks and display them visually on the screen, while also recording the output video.

The system uses computer vision techniques to process video frames and detect hand gestures dynamically.

## 🎯 Objectives

* Detect human hand in real-time
* Track finger positions using landmarks
* Display gesture visualization on screen
* Record video with hand and face visible
* Build a base for gesture-controlled applications

## 🛠️ Tools & Technologies Used

* 🐍 **Python 3.10** – Programming language
* 📷 **OpenCV (cv2)** – For video capture & display
* 🤖 **MediaPipe** – For hand tracking and landmark detection
* 💻 **VS Code** – Code editor
* 🎥 Webcam – Input device


## ⚙️ Libraries Used

* `cv2` → Camera handling & video recording
* `mediapipe` → Hand detection model


## 🔄 Working Process (Step-by-Step)

### 1️⃣ Capture Video

* Webcam captures live video using OpenCV

### 2️⃣ Frame Processing

* Each frame is flipped and converted from BGR → RGB

### 3️⃣ Hand Detection

* MediaPipe processes the frame and detects hand landmarks

### 4️⃣ Landmark Drawing

* 21 key points of the hand are drawn on the screen

---

## 💻 Installation Steps

🪜 Step 1: Install Python 3.10

 🪜 Step 2: Install Required Libraries

Open terminal and run:

py -3.10 -m pip install opencv-python mediapipe

🪜 Step 3: Verify Installation

py -3.10 -c "import cv2; import mediapipe as mp; print('All good')"

 ▶️ How to Run the Project

1. Open project folder in VS Code
2. Open terminal
3. Run:

```bash
py -3.10 hand_gesture.py
```

## ✨ Features

✔ Real-time hand tracking
✔ 21 landmark detection
✔ Live video display


## 🚀 Applications

* Gesture-controlled systems
* Virtual mouse / keyboard
* Gaming controls
* Sign language recognition
* Touchless interfaces

## 🧾 Conclusion

This project demonstrates how computer vision and machine learning can be used to build real-time interactive systems. It provides a strong foundation for developing advanced gesture-based applications.
