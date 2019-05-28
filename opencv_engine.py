import cv2
import sys

class HaarClassifier():
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

    def detectFace(self, grayFrame, outputFrame):
        scaleFactor = 1.15
        minNeighbors = 5
        faces = self.faceCascade.detectMultiScale(grayFrame, scaleFactor, minNeighbors)
        for (x, y, w, h) in faces:
            cv2.rectangle(outputFrame, (x, y), (x + w, y + h), (0, 255, 0), 2)

count = 0
class Recognize(HaarClassifier):
    def __init__(self):
        super().__init__()
        self.haarClassifier = HaarClassifier

    def capture(self):
        cap = cv2.VideoCapture(0)

        if cap.isOpened():
            return cap
        else:
            print('Failed')
            sys.exit()

    def start(self):
        cap = self.capture()
        while True:
            ret, img = cap.read()
            if ret:
                grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                self.haarClassifier.detectFace(grayScale, img)

                cv2.imshow('img', img)

                if (len(faces) != 0):
                    cv2.imwrite('face_image_%d.png' % count)
                    count += 1

                k = cv2.waitKey(1)
                if k == ord('q'):
                    break
                    
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    recognize = Recognize()
    recognize.start()
