# Итерируемый объект имет функцию __iter__, которая одновременно является генератором
class EvenSequence:

    def __init__(self, num):
        self.num = num
        self.i = -2

    def __iter__(self):
        while self.i < self.num:
            self.i += 2
            yield self.i


for x in EvenSequence(10):
    print(x, end=' ')
print('')

it = iter(EvenSequence(12))
while True:
    try:
        print(next(it), end=' ')
    except StopIteration:
        break
