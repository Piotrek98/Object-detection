import cv2
import wikipedia
import time

_wallclock = 0

class HaarClassifier_wallclock:
    def __init__(self):
        self.wallclockCascade = cv2.CascadeClassifier('data/wallclock.xml')

    def detectWallClock(self, grayFrame, outputFrame):
        scaleFactor = 1.15
        minNeighbors = 5
        wallclock = 'Wall clock'

        wallclocks = self.wallclockCascade.detectMultiScale(grayFrame, scaleFactor, minNeighbors)

        for (x, y, w, h) in wallclocks:
            outlined_image = cv2.rectangle(outputFrame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(outlined_image, wallclock, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

            if (len(wallclocks) != 0):
                global _wallclock
                _wallclock +=  1
                while _wallclock == 1:
                    print('[ ATTENTION ] DETECTED OBJECT')
                    time.sleep(.6)
                    print('---' * 25)
                    print(wikipedia.summary(wallclock, sentences = 1))
                    print('---' * 25)
                    print(wikipedia.page(wallclock).url)
                    print('---' * 25)
                    break





    #another haar methods...


    #and another...


    #and another...fullbody
