# Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.
# Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
# Решение оформите в виде функции swap_columns(a, i, j).
# Input:
# 3 4
# 11 12 13 14
# 21 22 23 24
# 31 32 33 34
# 0 1
# Output:
# 12 11 13 14
# 22 21 23 24
# 32 31 33 34
#
def swap_columns(a, col1, col2):
    for i in range(len(a)):
        a[i][col1], a[i][col2] = a[i][col2], a[i][col1]


n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
col1, col2 = [int(i) for i in input().split()]
swap_columns(a, col1, col2)
for row in a:
    print(*row)
