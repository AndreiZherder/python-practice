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


class EvenSequence:

    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return EvenIterator(self.num)


for x in EvenSequence(10):
    print(x)

lst = [1, 2, 3, 4, 5, 6]
it = iter(lst)
while True:
    try:
        print(next(it), end=' ')
    except StopIteration:
        break

