"""
Известно, что любую обыкновенную дробь можно записать в виде конечной простой непрерывной дроби.
https://en.wikipedia.org/wiki/Continued_fraction
Напишите программу, которая преобразует обыкновенную дробь в последовательность коэффициентов a_0, a_1, a_n
Формат ввода:
Строка, содержащая обыкновенную дробь в формате числитель/знаменатель.

Формат вывода:
Строка с последовательностью коэффициентов, записанных через пробел.

Sample Input:

239/30
Sample Output:

7 1 29
"""


def main():
    num, den = (int(i) for i in input().split('/'))
    ans = []
    rem = 1
    while rem != 0:
        rem = num % den
        a = num // den
        ans.append(a)
        num, den = den, num - a * den
    print(*ans)


if __name__ == '__main__':
    main()
