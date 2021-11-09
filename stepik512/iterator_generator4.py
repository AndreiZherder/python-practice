def even_generator(num: int):
    i = -2
    while i < num:
        i += 2
        yield i


for x in even_generator(10):
    print(x)
