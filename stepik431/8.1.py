"""
Напишите простой интерпретатор математического выражения.

На вход подаётся строка с выражением, состоящим из двух чисел, объединённых бинарным оператором.


Sample Input 1:

45 plus 8
Sample Output 1:

53
Sample Input 2:

12 minus 42
Sample Output 2:

-30
Sample Input 3:

451 multiply 2
Sample Output 3:

902
Sample Input 4:

13 divide 3
Sample Output 4:

4
"""
import operator


def main():
    d = {
        'plus': operator.add,
        'minus': operator.sub,
        'multiply': operator.mul,
        'divide': operator.floordiv,
    }
    a, op, b = input().split()
    print(d[op](int(a), int(b)))


if __name__ == '__main__':
    main()
