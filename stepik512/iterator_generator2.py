def even_generator(num: int):
    i = -2
    while i < num:
        i += 2
        yield i


class EvenSequence:

    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return even_generator(self.num)


for x in EvenSequence(10):
    print(x)
