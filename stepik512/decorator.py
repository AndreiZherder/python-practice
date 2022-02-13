import functools
from typing import List


def trace(s1, s2):
    def deco(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            print(s1)
            res = f(*args, **kwargs)
            print(s2)
            return res
        return wrapper
    return deco


def main():
    # @trace(s1='before', s2='after')
    def min(a: List[int]) -> int:
        ans = float('Inf')
        for num in a:
            if num < ans:
                ans = num
        return ans

    a = [1, 2, 3, 4, 5]
    deco = trace(s1='before', s2='after')
    min = deco(min)
    print(min.__name__)
    print(min(a))


if __name__ == '__main__':
    main()
