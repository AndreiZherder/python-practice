import functools


def header(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print(f'Table header')
        f(*args, **kwargs)

    return wrapper


@header
def table(a: dict):
    for k, v in a.items():
        print(f'{k} : {v}')


def coro(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        g = f(*args, **kwargs)
        g.send(None)
        return g

    return wrapper


@coro
def gtable(a: dict):
    message = yield
    for k, v in a.items():
        print(f'coro received message: {message}')
        message = yield f'{k} : {v}'


def main():
    a = {i: i * i for i in range(5)}
    table(a)
    print()

    i = 0
    gen = gtable(a)
    while True:
        try:
            print(gen.send(i))
            i += 1
        except StopIteration:
            break


if __name__ == '__main__':
    main()
