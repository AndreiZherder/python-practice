# Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке.
# В левом верхнем углу должна стоять точка.
# Input:
# 3 4
# Output:
# . * . *
# * . * .
# . * . *
#
n, m = [int(i) for i in input().split()]
a = [['.' if (i + j) % 2 == 0 else '*' for j in range(m)] for i in range(n)]
for row in a:
    print(' '.join(row))
