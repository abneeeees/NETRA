#!/usr/bin/env python3
import pyautogui
import os
import mediapipe as mp
import cv2
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.1, min_tracking_confidence=0.1) as hands:
    while True:
        suc, img = cap.read()
        img = cv2.flip(img, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img , dsize=(480 , 270))
        results = hands.process(img)

        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_position in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, hand_position, mp_hands.HAND_CONNECTIONS)

                landmarks = np.array([(lm.x, lm.y, lm.z) for lm in hand_position.landmark])

                index_tip = landmarks[8]
                x = index_tip[0]
                y = index_tip[1]

                width , height = pyautogui.size()
                screen_x = (x*width)
                screen_y = (y*height)

                pyautogui.moveTo(screen_x , screen_y)

        cv2.imshow("webcam", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
