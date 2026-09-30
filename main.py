import cv2
import mediapipe as mp
import math
import numpy as np

# ================= VOLUME CONTROL =================
from pycaw.pycaw import AudioUtilities

devices = AudioUtilities.GetSpeakers()
volume = devices.EndpointVolume
minVol, maxVol = volume.GetVolumeRange()[:2]

print("Audio device connected successfully.")
print(f"Volume range: {minVol:.2f} to {maxVol:.2f}")


# ================= MEDIAPIPE =================
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils


# ================= CAMERA =================
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("ERROR: Camera could not be opened.")
    exit()


# ================= MAIN LOOP =================
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    while True:

        success, img = cap.read()

        if not success:
            print("Camera frame could not be read.")
            break

        # Mirror camera
        img = cv2.flip(img, 1)

        # RGB conversion
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Hand detection
        results = hands.process(imgRGB)

        lmList = []

        if results.multi_hand_landmarks:

            handLms = results.multi_hand_landmarks[0]

            h, w, _ = img.shape

            # Draw hand skeleton
            mp_draw.draw_landmarks(
                img,
                handLms,
                mp_hands.HAND_CONNECTIONS
            )

            for id, lm in enumerate(handLms.landmark):

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                lmList.append((id, cx, cy))

        # ================= VOLUME CONTROL =================

        volume_percent = 0

        if len(lmList) >= 9:

            # Thumb
            x1, y1 = lmList[4][1:]

            # Index finger
            x2, y2 = lmList[8][1:]

            # Finger points
            cv2.circle(
                img,
                (x1, y1),
                10,
                (255, 255, 255),
                -1
            )

            cv2.circle(
                img,
                (x2, y2),
                10,
                (255, 255, 255),
                -1
            )

            # Connecting line
            cv2.line(
                img,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                3
            )

            # Calculate finger distance
            length = math.hypot(
                x2 - x1,
                y2 - y1
            )

            # System volume
            vol = np.interp(
                length,
                [30, 200],
                [minVol, maxVol]
            )

            volume.SetMasterVolumeLevel(
                float(vol),
                None
            )

            # Volume percentage
            volume_percent = int(
                np.interp(
                    length,
                    [30, 200],
                    [0, 100]
                )
            )

        # ================= UI =================

        # Semi-transparent top panel
        overlay = img.copy()

        cv2.rectangle(
            overlay,
            (0, 0),
            (img.shape[1], 85),
            (20, 20, 20),
            -1
        )

        img = cv2.addWeighted(
            overlay,
            0.75,
            img,
            0.25,
            0
        )

        # Title
        cv2.putText(
            img,
            "GESTURE VOLUME CONTROL",
            (25, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        # Volume text
        cv2.putText(
            img,
            f"VOLUME  {volume_percent}%",
            (25, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        # ================= VOLUME BAR =================

        bar_x = img.shape[1] - 75
        bar_top = 130
        bar_bottom = 430
        bar_width = 35

        # Bar background
        cv2.rectangle(
            img,
            (bar_x, bar_top),
            (bar_x + bar_width, bar_bottom),
            (40, 40, 40),
            -1
        )

        # Bar border
        cv2.rectangle(
            img,
            (bar_x, bar_top),
            (bar_x + bar_width, bar_bottom),
            (255, 255, 255),
            2
        )

        # Filled volume
        fill_height = int(
            (volume_percent / 100) *
            (bar_bottom - bar_top)
        )

        fill_top = bar_bottom - fill_height

        if fill_height > 0:

            cv2.rectangle(
                img,
                (bar_x + 3, fill_top),
                (bar_x + bar_width - 3, bar_bottom - 3),
                (0, 255, 0),
                -1
            )

        # Percentage beside bar
        cv2.putText(
            img,
            f"{volume_percent}%",
            (bar_x - 80, bar_bottom + 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2
        )

        # ================= INSTRUCTIONS =================

        cv2.putText(
            img,
            "Move thumb + index finger",
            (25, img.shape[0] - 45),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

        cv2.putText(
            img,
            "Press Q to quit",
            (25, img.shape[0] - 18),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (200, 200, 200),
            1
        )

        # ================= DISPLAY =================

        cv2.imshow(
            "Gesture Volume Control",
            img
        )

        # Quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


# ================= CLEANUP =================

cap.release()
cv2.destroyAllWindows()