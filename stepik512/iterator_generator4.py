# Генератор может быть вызван по функции __next__
# Возвращает очередное значение по оператору yield и бросает StopIteration при выходе из функции
def even_generator(num: int):
    i = -2
    while i < num:
        i += 2
        yield i


it = iter(even_generator(12))
while True:
    try:
        print(next(it), end=' ')
    except StopIteration:
        break

print('')
y = even_generator(10)
for x in y:
    print(x, end=' ')

print('')
for x in y:  # second time y is empty
    print(x, end=' ')

