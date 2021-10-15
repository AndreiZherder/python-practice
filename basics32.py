# Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (число повторяется столько раз, чему равно).
# На вход программе передаётся неотрицательное целое число n —
# столько элементов последовательности должна отобразить программа.
# На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
#
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
# input:
# 7
# output:
# 1 2 2 3 3 3 4
n = int(input())
a = []
i = 1
while len(a) < n:
    j = 0
    while len(a) < n and j < i:
        a.append(i)
        j += 1
    i += 1
print(*a)
