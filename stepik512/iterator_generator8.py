# Генератор может быть вызван по функции __next__
# Возвращает очередное значение по оператору yield и бросает StopIteration при выходе из функции
def even_generator(num: int):
    i = -2
    while i < num:
        i += 2
        request = yield i
        print(f'generator received request: {request}')


def main():
    gen = even_generator(10)
    cnt = 0
    try:
        num = gen.send(None)
        print(f'num = {num}')
        while True:
            num = gen.send(cnt)
            print(f'num = {num}')
            cnt += 1
    except StopIteration:
        pass


if __name__ == '__main__':
    main()
