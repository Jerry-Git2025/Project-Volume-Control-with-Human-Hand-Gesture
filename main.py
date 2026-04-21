import cv2
import mediapipe as mp
import math
import numpy as np

# Volume control (Windows)
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# ---------------- VOLUME SETUP ----------------
devices = AudioUtilities.GetSpeakers()

interface = devices.Activate(
    IAudioEndpointVolume._iid_,
    CLSCTX_ALL,
    None
)

volume = cast(interface, POINTER(IAudioEndpointVolume))
minVol, maxVol = volume.GetVolumeRange()[:2]

# ---------------- MEDIAPIPE SETUP ----------------
from mediapipe import solutions as mp_solutions
mp_hands = mp_solutions.hands
mp_draw = mp_solutions.drawing_utils

# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# ---------------- MAIN LOOP ----------------
with mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    while True:
        success, img = cap.read()
        if not success:
            print("Camera not working")
            break

        img = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        lmList = []

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(
                    img, handLms, mp_hands.HAND_CONNECTIONS
                )

                for id, lm in enumerate(handLms.landmark):
                    h, w, _ = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append((id, cx, cy))

        if lmList:
            x1, y1 = lmList[4][1:]
            x2, y2 = lmList[8][1:]

            # Draw points
            cv2.circle(img, (x1, y1), 10, (255, 255, 255), -1)
            cv2.circle(img, (x2, y2), 10, (255, 255, 255), -1)
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

            # Distance
            length = math.hypot(x2 - x1, y2 - y1)

            # Volume control
            vol = np.interp(length, [30, 200], [minVol, maxVol])
            volume.SetMasterVolumeLevel(vol, None)

            # UI
            volPer = np.interp(length, [30, 200], [0, 100])
            volBar = np.interp(length, [30, 200], [400, 150])

            cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 0), 3)
            cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 0, 0), -1)

            cv2.putText(
                img,
                f'{int(volPer)}%',
                (40, 450),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2
            )

        cv2.imshow("Gesture Volume Control", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()