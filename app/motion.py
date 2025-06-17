#! /usr/bin/env python3 

from model import *

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
