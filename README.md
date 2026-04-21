# Gesture Volume Control 🎚️

Control your system volume using hand gestures in real-time.

---

## 🚀 Features

* Real-time hand tracking
* Volume control using finger distance
* Smooth UI feedback

---

## 🛠️ Tech Stack

* Python 3.10
* OpenCV
* MediaPipe
* Pycaw (Windows)

---

## 📦 How to Run (IMPORTANT)

### 1. Clone the repository

```bash
git clone https://github.com/Jerry-Git2025/Project-Volume-Control-with-Human-Hand-Gesture.git
cd Project-Volume-Control-with-Human-Hand-Gesture
```

### 2. Create virtual environment

```bash
py -3.10 -m venv .venv
```

### 3. Activate environment

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install opencv-python mediapipe numpy pycaw comtypes
```

### 5. Run the project

```bash
python main.py
```

---

## 🎯 How it Works

* Detects hand using MediaPipe
* Tracks thumb & index finger
* Calculates distance
* Maps distance → system volume

---

## ⚠️ Requirements

* Windows OS
* Python 3.10
* Webcam

---

## 📌 Future Improvements

* Mute gesture
* Media control
* Brightness control
