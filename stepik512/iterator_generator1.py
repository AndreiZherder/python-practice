# Итератор выделен в отдельный класс, имеющий функцию __next__
class EvenIterator:

    def __init__(self, num):
        self.num = num
        self.i = -2

    def __next__(self):
        self.i += 2
        if self.i < self.num:
            return self.i
        else:
            raise StopIteration


# Итерируемый объект имеет функцию __iter__
class EvenSequence:

    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return EvenIterator(self.num)


for x in EvenSequence(10):
    print(x, end=' ')
print('')

it = iter(EvenSequence(12))
while True:
    try:
        print(next(it), end=' ')
    except StopIteration:
        break
