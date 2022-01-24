"""
Измерить время выполнения функции
"""
import random
import time
from typing import List
import matplotlib.pyplot as plt


def timed(f, *args):
    acc = float('Inf')
    for _ in range(500):
        t1 = time.perf_counter_ns()
        f(*args)
        t2 = time.perf_counter_ns()
        acc = min(acc, t2 - t1)
    return acc


def slice_func(s: str, pattern: str, i: int):
    if s[i:i + len(pattern)] == pattern:
        print('!!!')


def index_func(s: str, pattern: str, i: int):
    for j in range(len(pattern)):
        if s[i + j] != pattern[j]:
            break
    else:
        print('!!!')


def enumerate_func(s: str, pattern: str, i: int):
    for j, c in enumerate(pattern):
        if s[i + j] != c:
            break
    else:
        print('!!!')


def main():
    n = 1000
    s = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(n + 100))
    pattern = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(100))
    fig, ax = plt.subplots()
    ax.plot(list(range(n)), [timed(slice_func, s, pattern, i) for i in range(n)], 'g')
    ax.plot(list(range(n)), [timed(index_func, s, pattern, i) for i in range(n)], 'r')
    ax.plot(list(range(n)), [timed(enumerate_func, s, pattern, i) for i in range(n)], 'b')
    ax.set_xlabel('n')
    ax.set_ylabel('time, ns')
    ax.set_title('Execution time')
    ax.grid()
    fig.show()


if __name__ == '__main__':
    main()
