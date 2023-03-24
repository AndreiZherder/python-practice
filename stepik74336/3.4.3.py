import sys
from itertools import accumulate

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, d = [int(num) for num in input().split()]
    a = list(accumulate((int(num) for num in input().split()), initial=0))
    i = 0
    j = 0
    for i in range(n):
        while a[j] - a[i] < d:
            j += 1
        if a[j] - a[i] == d:
            break
    print(i + 1, j + 1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
