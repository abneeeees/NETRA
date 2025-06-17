#! usr/bin/env python3

from model import *
from motion import Cursor , Navigator

def main():

    cam = VideoCamera()
    tracker = HandTrackingModule()
    mover1 = Cursor()
    mover2 = Navigator()

    while True:
        frame = cam.get_frame()
        processed_frame, new_landmarks = tracker.hand_tracing(frame)
        
        # mover1.cursor_move(new_landmarks)
        mover2.window_move(new_landmarks)
        cam.run_camera(new_frame=processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break    
    
if __name__ == '__main__':
    main()