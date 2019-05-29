import cv2
import sys

class HaarClassifier:
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

    def detectFace(self, grayFrame, outputFrame):
        scaleFactor = 1.2
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


        try:
            if cap.isOpened():
                return cap
            else:
                print("Failed to load")
                sys.exit()
        except:
            print('Failed to load')

    def start(self):
        cap = self.capture()
        while True:
            ret, img = cap.read()
            if ret:
                grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                self.haarClassifier.detectFace(grayScale, img)

                cv2.imshow('img', img)
                k = cv2.waitKey(1)
                if k == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    recognition = Recognition()
    recognition.start()
