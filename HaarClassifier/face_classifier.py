import cv2
import wikipedia
import time

count = 0

class HaarClassifier_face:
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

    def detectFace(self, grayFrame, outputFrame):
        scaleFactor = 1.15
        minNeighbors = 5
        face = 'Face'

        faces = self.faceCascade.detectMultiScale(grayFrame, scaleFactor, minNeighbors)

        for (x, y, w, h) in faces:
            outlined_image = cv2.rectangle(outputFrame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(outlined_image, face, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

            if (len(faces) != 0):
                global count
                count +=  1
                while count == 1:
                    print('[ ATTENTION ] DETECTED OBJECT')
                    time.sleep(.6)
                    print('---' * 25)
                    print(wikipedia.summary(face, sentences = 1))
                    print('---' * 25)
                    print(wikipedia.page(face).url)
                    print('---' * 25)
                    break





    #another haar methods...


    #and another...


    #and another...
