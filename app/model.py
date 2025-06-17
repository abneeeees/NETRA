# !/usr/bin/env python3
import pyautogui
import mediapipe as mp
import cv2
import numpy as np
pyautogui.FAILSAFE = False


class VideoCamera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.suc , self.img = self.cap.read()

    def get_frame(self):
        self.suc , self.img = self.cap.read()
        if self.suc:
            self.img = cv2.flip(self.img, 1)
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            return self.img 
        return None
    
    def run_camera(self , new_frame):
        cv2.imshow("webcam" , new_frame )
    
class HandTrackingModule(VideoCamera):
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1 ,
                                          min_detection_confidence=0.5,
                                            min_tracking_confidence=0.5)

    def hand_tracing(self , img):
        results = self.hands.process(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks: 
            for hand_position in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(img , hand_position , self.mp_hands.HAND_CONNECTIONS)
                landmarks = np.array([(lm.x , lm.y , lm.z) for lm in hand_position.landmark])
                return img , landmarks
        return img , None


