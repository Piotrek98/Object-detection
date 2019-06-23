import cv2
import wikipedia
import time

_car = 0

class HaarClassifier_car:
    def __init__(self):
        self.carCascade = cv2.CascadeClassifier('data/car.xml')

    def detectCar(self, grayFrame, outputFrame):
        scaleFactor = 1.15
        minNeighbors = 5
        car = 'Car'

        cars = self.carCascade.detectMultiScale(grayFrame, scaleFactor, minNeighbors)

        for (x, y, w, h) in cars:
            outlined_image = cv2.rectangle(outputFrame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(outlined_image, car, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

            if (len(cars) != 0):
                global _car
                _car +=  1
                while _car == 1:
                    print('[ ATTENTION ] DETECTED OBJECT')
                    time.sleep(.6)
                    print('---' * 25)
                    print(wikipedia.summary(car, sentences = 1))
                    print('---' * 25)
                    print(wikipedia.page(car).url)
                    print('---' * 25)
                    break





    #another haar methods...


    #and another...


    #and another...
