# Напишите программу, вычисляющую площадь треугольника по переданным длинам трёх его сторон по формуле Герона:
# Sample Input:
# 3
# 4
# 5
# Sample Output:
# 6.0
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(s)
