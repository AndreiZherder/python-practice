# Реализуйте программу, которая принимает последовательность чисел и выводит их сумму.
#
# Вашей программе на вход подается последовательность строк.
# Первая строка содержит число n (1 ≤ n ≤ 100).
# В следующих n строках содержится по одному целому числу.
#
# Выведите одно число – сумму данных n чисел.
n = int(input())
sum = 0
for _ in range(n):
    sum += int(input())
print(sum)
