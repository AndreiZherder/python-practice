# Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел, которые нужно считать.
# Далее считывает n строк с числами x_i, по одному числу в каждой строке. Итого будет n+1 строк.
#
# При считывании числа x_i программа должна на отдельной строке вывести значение f(x_i).
# Функция f(x) уже реализована и доступна для вызова.
# Функция вычисляется достаточно долго и зависит только от переданного аргумента x.
# Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.
# Sample Input:
#
# 5
# 5
# 12
# 9
# 20
# 12
# Sample Output:
#
# 11
# 41
# 47
# 61
# 41
def f(x):
    return x * x


res = dict()
for i in range(int(input())):
    x = int(input())
    if x not in res:
        res[x] = f(x)
    print(res[x])
