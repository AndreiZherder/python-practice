class EvenSequence:

    def __init__(self, num):
        self.num = num
        self.i = -2

    def __iter__(self):
        while self.i < self.num:
            self.i += 2
            yield self.i


for x in EvenSequence(10):
    print(x)
