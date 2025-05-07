# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.
import time

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            current_value = self.current
            self.current -= 1
            return current_value

c1 = Countdown(5)

for number in c1:
    time.sleep(0.5)
    print(number)







