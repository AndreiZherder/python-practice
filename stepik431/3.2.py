"""
Напишите функцию f(x), принимающую дробное число x и возвращающую значение следующей функции,
определённой на всей числовой прямой:
1 - (x + 2) * (x + 2), x <= -2
-x / 2, -2 < x <= 2
(x - 2) * (x- 2) + 1, x > 2

Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.

Sample Input 1:

4.5
Sample Output 1:

7.25
Sample Input 2:

-4.5
Sample Output 2:

-5.25
Sample Input 3:

1.0
Sample Output 3:

-0.5
"""


def f(x):
    if x <= -2:
        return 1 - (x + 2) * (x + 2)
    elif x <= 2:
        return -x / 2
    else:
        return (x - 2) * (x - 2) + 1


def main():
    print(f(4.5), f(-4.5), f(1.0))


if __name__ == '__main__':
    main()
