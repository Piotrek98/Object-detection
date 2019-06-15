import wikipedia
import time

from classifier import HaarClassifier

count = 0

class search:
    def __init__(self):
        super().__init__()
        self.haarClassifier = HaarClassifier()

    def wikipedia(self):
        while count == 1:
            print('[ ATTENTION ] DETECTED OBJECT')
            time.sleep(.6)
            print('---' * 25)
            print(wikipedia.summary(query, sentences = 1))
            print('---' * 25)
            print(wikipedia.page(query).url)
            print('---' * 25)
            break
