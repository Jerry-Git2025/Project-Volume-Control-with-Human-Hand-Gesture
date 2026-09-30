# 🎚️ Project Volume Control with Human Hand Gesture

Control your **Windows system volume using hand gestures**.

This project uses your webcam to detect your hand with **MediaPipe**. The distance between your **thumb and index finger** controls the system volume:

* 🤏 Fingers close together → Lower volume
* 🖐️ Fingers farther apart → Higher volume

The project also includes a clean camera UI showing the current volume percentage.

---

## ✨ Features

* 🎥 Real-time hand tracking using your webcam
* ✋ Thumb + index finger gesture control
* 🔊 Controls Windows system volume
* 📊 Clean volume indicator
* 🖥️ Real-time camera interface
* 🚫 Distance value is not displayed
* ⚡ Real-time response
* ⌨️ Press `Q` to quit

---

## 🖼️ How It Works

The application detects the following MediaPipe hand landmarks:

* **Landmark 4** → Thumb tip
* **Landmark 8** → Index finger tip

The distance between these two points is converted into a Windows volume level.

```text
Thumb ●────────────● Index
       ← Distance →

Short distance  → 🔉 Low volume
Long distance   → 🔊 High volume
```

The distance is used internally for volume control but is **not displayed on the camera screen**.

---

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy
* Pycaw
* Windows Core Audio

---

# 💻 Requirements

## Operating System

**Windows 10 or Windows 11**

> Pycaw is designed specifically for Windows audio control, so this project is currently Windows-only.

## Python

Recommended:

**Python 3.10.x**

The tested environment for this project uses:

```text
Python 3.10
MediaPipe 0.10.21
NumPy 1.26.4
OpenCV 4.10.0.84
```

MediaPipe 0.10.21 provides a CPython 3.10 Windows wheel, making Python 3.10 a supported setup for this project.

---

# 📦 Installation

## 1. Clone the repository

```bash
git clone https://github.com/Jerry-Git2025/Project-Volume-Control-with-Human-Hand-Gesture.git
```

Enter the project directory:

```bash
cd Project-Volume-Control-with-Human-Hand-Gesture
```

---

## 2. Create a virtual environment

It is strongly recommended to use a virtual environment.

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

If you are using Command Prompt:

```cmd
.venv\Scripts\activate
```

---

## 3. Install dependencies

Run:

```bash
python -m pip install --upgrade pip
```

Then:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains the tested dependency versions for this project.

---

# ▶️ Run the Project

Run:

```bash
python main.py
```

A camera window will open.

Show your hand to the camera and move your:

**Thumb ↔ Index Finger**

to control the volume.

### Controls

| Action              | Result             |
| ------------------- | ------------------ |
| Move fingers closer | 🔉 Decrease volume |
| Move fingers apart  | 🔊 Increase volume |
| Press `Q`           | Exit application   |

---

# 🎨 User Interface

The camera interface displays:

```text
GESTURE VOLUME CONTROL
VOLUME XX%
```

A vertical volume bar shows the current volume level.

The actual finger distance is calculated internally but **is intentionally not displayed**.

---

# 📁 Project Structure

```text
Project-Volume-Control-with-Human-Hand-Gesture/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚠️ Troubleshooting

## MediaPipe error

If you see:

```text
AttributeError: module 'mediapipe' has no attribute 'solutions'
```

make sure the project is using:

```text
mediapipe==0.10.21
```

Check your installed version:

```bash
python -c "import mediapipe as mp; print(mp.__version__)"
```

It should show:

```text
0.10.21
```

---

## NumPy compatibility error

This project uses:

```text
numpy==1.26.4
```

Do not manually upgrade NumPy to version 2.x for this setup.

Check the installed version:

```bash
python -c "import numpy; print(numpy.__version__)"
```

Expected:

```text
1.26.4
```

---

## Camera does not open

The project uses:

```python
cv2.VideoCapture(0, cv2.CAP_DSHOW)
```

If your computer has multiple cameras, you may need to change:

```python
cv2.VideoCapture(0, cv2.CAP_DSHOW)
```

to:

```python
cv2.VideoCapture(1, cv2.CAP_DSHOW)
```

Also make sure Windows camera permissions are enabled.

---

## Volume does not change

Make sure:

* You are running Windows.
* A working audio output device is connected.
* Windows has allowed Python to access the audio device.
* Your hand is visible to the camera.
* Your thumb and index finger are both detected.

---

# 🔒 Platform Support

| Platform   | Supported |
| ---------- | --------- |
| Windows 10 | ✅         |
| Windows 11 | ✅         |
| Linux      | ❌         |
| macOS      | ❌         |

The Windows-only limitation comes from the use of Pycaw for Windows Core Audio control.

---

# 📌 Tested Environment

This project was tested with:

```text
OS: Windows
Python: 3.10.x
MediaPipe: 0.10.21
NumPy: 1.26.4
OpenCV: 4.10.0.84
Pycaw: Latest compatible release
```

---

# 🚀 Future Improvements

Possible future additions:

* 🔇 Gesture-based mute/unmute
* 🎵 Application-specific volume control
* 👋 Multiple gesture commands
* 🎨 More UI themes
* 📱 Better camera controls
* 🖥️ Desktop GUI
* 🔊 Volume smoothing to reduce rapid changes

---

# 📄 License

This project is available for learning and personal use.

Feel free to modify and improve it.

---

## ⭐ If this project helped you

Consider giving the repository a ⭐ on GitHub!

**Repository:**
https://github.com/Jerry-Git2025/Project-Volume-Control-with-Human-Hand-Gesture

## ▶️ How to Run

1. Clone repo:
git clone https://github.com/Jerry-Git2025/Project-Volume-Control-with-Human-Hand-Gesture

2. Go inside folder:
cd Project-Volume-Control-with-Human-Hand-Gesture

3. Install dependencies:
pip install -r requirements.txt

4. Run project:
python volume_control.py

