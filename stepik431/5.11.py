"""
Последовательность n, n>0 целых чисел называется jolly jumper в случае,
если значения абсолютных разностей последовательных элементов принимают все возможные значения между 1 и n-1.

Например, последовательность 1 -3 -4 -1 1 является jolly jumper последовательностью,
так как абсолютные разности равны 4 1 3 2, соответственно, а n-1 = 4.
Будем считать, что последовательность из одного числа является jolly jumper.

Напишите программу, которая проверяет, является ли введённая последовательность jolly jumper.

Формат ввода:

Строка, содержащая 1 <= n <= 10000 целых чисел, разделённых пробелом.

Формат вывода:
Одна строка, содержащая "Jolly" (без кавычек),
если последовательность является jolly jumper и "Not jolly" в противном случае.

Sample Input 1:

1 -3 -4 -1 1
Sample Output 1:

Jolly
Sample Input 2:

1 3 5
Sample Output 2:

Not jolly
Sample Input 3:

4
Sample Output 3:

Jolly
"""


def main():
    nums = [int(_) for _ in input().split()]
    n = len(nums)
    if n == 1:
        print('Jolly')
        return
    d = [0 for _ in range(n - 1)]
    for i in range(1, n):
        sub = abs(nums[i] - nums[i - 1])
        if sub > n - 1:
            print('Not jolly')
            return
        if d[sub - 1] == 1:
            print('Not jolly')
            return
        else:
            d[sub - 1] = 1
    print('Jolly')


if __name__ == '__main__':
    main()
