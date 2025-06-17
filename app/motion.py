#! /usr/bin/env python3 

from model import *
from collections import deque
import os

class Cursor(HandTrackingModule):
    def cursor_move(self , landmarks):
        if landmarks is not None:
            index_tip = landmarks[8]
            x = index_tip[0]
            y = index_tip[1]
 
            width , height = pyautogui.size()
            screen_x = (x*width)
            screen_y = (y*height) 
            pyautogui.moveTo(screen_x , screen_y)


class Navigator:
    def __init__(self):
        self.positions = deque(maxlen=10)

    def window_move(self , landmarks):
        if landmarks is not None:
            x, y = landmarks[8][0], landmarks[8][1]
            self.positions.append((x, y))

            if len(self.positions) == self.positions.maxlen:
                dx = self.positions[-1][0] - self.positions[0][0]
                dy = self.positions[-1][1] - self.positions[0][1]

                if abs(dx) > abs(dy): 
                    if dx > 0.1:
                        os.system('xdotool set_desktop 1')
                    elif dx < -0.1:
                        os.system('xdotool set_desktop 0')
                else:  
                    if dy > 0.1:
                        print('down')
                    elif dy < -0.1:
                        os.system('xdotool key Super_L')

q