# Найдите индексы первого вхождения максимального элемента.
# Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве.
# Если таких элементов несколько, то выводится тот, у которого меньше номер строки,
# а если номера строк равны то тот, у которого меньше номер столбца.
# Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.
# Input:
# 3 4
# 0 3 2 4
# 2 3 5 5
# 5 1 2 3
# Output:
# 1 2
#
n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
maxi = n - 1
maxj = m - 1
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if a[i][j] >= a[maxi][maxj]:
            maxi = i
            maxj = j
print(maxi, maxj)

