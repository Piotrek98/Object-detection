import cv2
import sys
import time

count = 0
class HaarClassifier:
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

    def detectFace(self, grayFrame, outputFrame):
        scaleFactor = 1.05
        minNeighbors = 5
        faces = self.faceCascade.detectMultiScale(grayFrame, scaleFactor, minNeighbors)

        for (x, y, w, h) in faces:
            outlined_image = cv2.rectangle(outputFrame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(outlined_image, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

class Recognition:
    def __init__(self):
        super().__init__()
        self.haarClassifier = HaarClassifier()

    def capture(self):
        cap = cv2.VideoCapture(0) #0 for online camera

        if cap.isOpened():
            return cap
        else:
            print("[ ERROR ] FAILED TO qqLOAD. CHECK YOUR CODE OR CURRENT PYTHON LIBRARIES.")
            sys.exit()

    def start(self):
        cap = self.capture()
        print('[ WARN ] PRESS Q TO SHUTDOWN PROGRAM')
        try:
            while True:
                ret, img = cap.read()
                if ret:
                    grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                    self.haarClassifier.detectFace(grayScale, img)

                    cv2.imshow('img', img)

                    #if (len(faces) != 0):
                    #    count +=  1
                    #    print('jest dobrze')
                    #    print(count)

                    k = cv2.waitKey(1)
                    if k == ord('q'):
                        print('[ WARN ] PROGRAM SHUTDOWN ...')
                        time.sleep(.5)
                        print('[ EXIT ]')
                        time.sleep(.9)
                        break
        except:
            print('[ ERROR ] PROGRAM SHUTDOWN. CHECK YOUR CODE OR CURRENT PYTHON LIBRARIES.')
            sys.exit()

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    recognition = Recognition()
    recognition.start()
