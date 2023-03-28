import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():

    n = int(input())
    a = [int(num) for num in input().split()]
    d = defaultdict(list)
    ans = []
    for i, prev in enumerate(a, start=1):
        d[prev].append(i)
    for prev in range(n + 1):
        stack = []
        while d[prev] or stack:
            if d[prev]:
                next = d[prev].pop()
                ans.append(next)
                stack.append(prev)
                prev = next
            else:
                prev = stack.pop()
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
