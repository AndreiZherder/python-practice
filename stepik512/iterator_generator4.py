# Генератор может быть вызван по функции __next__
# Возвращает очередное значение по оператору yield и бросает StopIteration при выходе из функции
def even_generator(num: int):
    i = -2
    while i < num:
        i += 2
        yield i


for x in even_generator(10):
    print(x, end=' ')
print('')

it = iter(even_generator(12))
while True:
    try:
        print(next(it), end=' ')
    except StopIteration:
        break
