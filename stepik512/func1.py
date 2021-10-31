def table3(a: str, b: str, c: str):
    print(a, b, c)


def mymin(*args):
    if not args:
        return
    min = args[0]
    for arg in args:
        if arg < min:
            min = arg
    return min


def myprint(d: dict):
    for item in d.items():
        print(item[0], item[1])


def myprint2(**kwargs):
    for item in kwargs.items():
        print(item[0], item[1])


d = {'a': 'morning', 'b': 'day', 'c': 'evening'}
table3(**d)
print(mymin(*d.values()))
print(mymin())
myprint(d)
myprint2(**d)
