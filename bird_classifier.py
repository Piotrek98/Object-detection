import cv2
import wikipedia
import time

_bird = 0

class HaarClassifier_bird:
    def __init__(self):
        self.birdCascade = cv2.CascadeClassifier('data/bird.xml')

    def detectBird(self, grayFrame, outputFrame):
        scaleFactor = 1.15
        minNeighbors = 5
        bird = 'Bird'

        birds = self.birdCascade.detectMultiScale(grayFrame, scaleFactor, minNeighbors)

        for (x, y, w, h) in birds:
            outlined_image = cv2.rectangle(outputFrame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(outlined_image, bird, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

            if (len(birds) != 0):
                global _bird
                _bird +=  1
                while _bird == 1:
                    print('[ ATTENTION ] DETECTED OBJECT')
                    time.sleep(.6)
                    print('---' * 25)
                    print(wikipedia.summary(bird, sentences = 1))
                    print('---' * 25)
                    print(wikipedia.page(bird).url)
                    print('---' * 25)
                    break





    #another haar methods...


    #and another...


    #and another...
