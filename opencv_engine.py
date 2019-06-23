#python opencv_engine.py --camera 0

import cv2
import sys
import time
import argparse

from HaarClassifier.face_classifier import HaarClassifier_face
#from HaarClassifier.bird_classifier import HaarClassifier_bird
#from HaarClassifier.car_classifier import HaarClassifier_car
#from HaarClassifier.fullbody_classifier import HaarClassifier_fullbody
#from HaarClassifier.wallclock_classifier import HaarClassifier_wallclock


ap = argparse.ArgumentParser()
ap.add_argument("-c", "--camera", type=int, required = True,
        help = "zero for online camera")
#ap.add_argument("-i", "--image", required=True,
#        help = "Path to the image")
args = vars(ap.parse_args())


class Recognition():
    def __init__(self):
        super().__init__()
        self.haarClassifier_face = HaarClassifier_face()
        #self.haarClassifier_bird = HaarClassifier_bird()
        #self.haarClassifier_car = HaarClassifier_car()
        #self.haarClassifier_fullbody = HaarClassifier_fullbody()
        #self.HaarClassifier_wallclock = HaarClassifier_wallclock()



    def capture(self):
        cap = cv2.VideoCapture(args["camera"]) # ["image"] for upload image in cmd


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

                self.haarClassifier_face.detectFace(grayScale, img)
                #self.haarClassifier_bird.detectBird(grayScale, img)
                #self.haarClassifier_car.detectCar(grayScale, img)
                #self.haarClassifier_fullbody.detectFullBody(grayScale, img)
                #self.HaarClassifier_wallclock.detectWallClock(grayScale, img)


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
