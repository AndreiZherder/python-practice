from functools import wraps


def trace(s1: str, s2: str):
    def deco(func):
        @wraps(func)
        def inner(*args):
            print(s1)
            func(*args)
            print(s2)

        return inner

    return deco


@trace('Hello!', 'Bye!')
def f(s: str):
    """prints a string"""
    print(s)


f('Andrei')
print(f.__doc__)


def trace1(s1: str, s2: str):
    def deco(func):
        @wraps(func)
        def inner(*args):
            print(s1)
            func(*args)
            print(s2)

        return inner

    return deco


def q(s: str):
    """prints a string"""
    print(s)


deco = trace1('Hello!', 'Bye!')
q = deco(q)
q('Andrei')
print(q.__doc__)


def coroutine(func):
    @wraps(func)
    def inner(*args):
        g = func(*args)
        next(g)
        return g
    return inner


@coroutine
def count(start=0):
    print('Init')
    yield
    while True:
        yield start
        start += 1


c1 = count(1)
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
