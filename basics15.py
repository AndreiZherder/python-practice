# Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.
# Используйте метод split строки.
numbers = [int(number) for number in input().split()]
sum = 0
for number in numbers:
    sum += number
print(sum)





