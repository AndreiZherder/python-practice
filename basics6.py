# Напишите программу, которая получает на вход три целых числа, по одному числу в строке,
# и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
# На ввод могут подаваться и повторяющиеся числа.
a = int(input())
b = int(input())
c = int(input())
if c > b:
    tmp = b
    b = c
    c = tmp
if b > a:
    tmp = a
    a = b
    b = tmp
if c > b:
    tmp = b
    b = c
    c = tmp
print(a)
print(c)
print(b)
