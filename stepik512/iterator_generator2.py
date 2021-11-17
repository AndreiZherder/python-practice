# Генератор может быть вызван по функции __next__
# Возвращает очередное значение по оператору yield и бросает StopIteration при выходе из функции
def even_generator(num: int):
    i = -2
    while i < num:
        i += 2
        yield i


# Итерируемый объект имет функцию __iter__
class EvenSequence:

    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return even_generator(self.num)


it = iter(EvenSequence(12))
while True:
    try:
        print(next(it), end=' ')
    except StopIteration:
        break

print('')
y = EvenSequence(10)
for x in y:
    print(x, end=' ')

print('')
for x in y:
    print(x, end=' ')
