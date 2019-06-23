import cv2
import wikipedia
import time

_fullbody = 0

class HaarClassifier_fullbody:
    def __init__(self):
        self.fullbodyCascade = cv2.CascadeClassifier('data/fullbody.xml')

    def detectFullBody(self, grayFrame, outputFrame):
        scaleFactor = 1.15
        minNeighbors = 5
        fullbody = 'People'

        fullbodys = self.fullbodyCascade.detectMultiScale(grayFrame, scaleFactor, minNeighbors)

        for (x, y, w, h) in fullbodys:
            outlined_image = cv2.rectangle(outputFrame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(outlined_image, fullbody, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

            if (len(fullbodys) != 0):
                global _fullbody
                _fullbody +=  1
                while _fullbody == 1:
                    print('[ ATTENTION ] DETECTED OBJECT')
                    time.sleep(.6)
                    print('---' * 25)
                    print(wikipedia.summary(fullbody, sentences = 1))
                    print('---' * 25)
                    print(wikipedia.page(fullbody).url)
                    print('---' * 25)
                    break





    #another haar methods...


    #and another...


    #and another...fullbody
