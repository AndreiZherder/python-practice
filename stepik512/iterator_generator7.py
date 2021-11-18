import itertools

lst = list(range(10))
print(*lst)
print(*map(lambda x, y: x * y, lst, itertools.repeat(2)))
print(*map(lambda x, y: x * y, lst, itertools.cycle([1, -1])))
print(*map(lambda x, y: x * y, lst, itertools.count()))
print(*itertools.accumulate(lst))
print(*itertools.chain(lst, range(9, -1, -1)))
print(*filter(lambda x: x % 2 == 0, lst))
print(*itertools.filterfalse(lambda x: x % 2 == 0, lst))
print(*itertools.compress(lst, (0 if i % 2 == 1 else 1 for i in range(10))))
print(*itertools.dropwhile(lambda x: x < 5, lst))
print(*itertools.takewhile(lambda x: x < 5, lst))


