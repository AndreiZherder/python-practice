import itertools

with open('../data/Bible.txt', 'r') as f:
    for pos, line in itertools.islice(enumerate(f), 500, 1000):
        print(pos, line)
