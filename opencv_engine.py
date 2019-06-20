#python opencv_engine.py --camera 0

import cv2
import sys
import time
import argparse

from search import search
from classifier import HaarClassifier


ap = argparse.ArgumentParser()
ap.add_argument("-c", "--camera", type=int, required = True,
        help = "zero for online camera")
#ap.add_argument("-i", "--image", required=True,
#        help = "Path to the image")
args = vars(ap.parse_args())

class Recognition(HaarClassifier):
    def __init__(self):
        super().__init__()
        self.haarClassifier = HaarClassifier()

    def capture(self):
        cap = cv2.VideoCapture(args["camera"]) #0 for online camera

        if cap.isOpened():
            return cap
        else:
            print("[ ERROR ] FAILED TO LOAD. CHECK YOUR CODE OR CURRENT PYTHON LIBRARIES.")
            sys.exit()

    def start(self):
        cap = self.capture()
        print('[ WARN ] PRESS Q TO SHUTDOWN PROGRAM')


        while True:
            ret, img = cap.read()
            if ret:
                grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                self.haarClassifier.detectFace(grayScale, img)

                cv2.imshow('img', img)


                k = cv2.waitKey(1)
                if k == ord('q'):
                    print('[ WARN ] PROGRAM SHUTDOWN ...')
                    time.sleep(.5)
                    print('[ EXIT ]')
                    time.sleep(.9)
                    break

        print('[ ERROR ] PROGRAM SHUTDOWN. CHECK YOUR CODE OR CURRENT PYTHON LIBRARIES.')
        sys.exit()

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    recognition = Recognition()
    recognition.start()
