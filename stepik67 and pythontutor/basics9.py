# В Институте биоинформатики между информатиками и биологами устраивается соревнование.
# Победителям соревнования достанется большой и вкусный пирог.
# В команде биологов aa человек, а в команде информатиков — bb человек.

# Нужно заранее разрезать пирог таким образом, чтобы можно было раздать кусочки пирога любой команде,
# выигравшей соревнование, при этом каждому участнику этой команды должно достаться одинаковое число кусочков пирога.
# И так как не хочется резать пирог на слишком мелкие кусочки, нужно найти минимальное подходящее число.

# Напишите программу, которая помогает найти это число.
# Программа должна считывать размеры команд
# (два положительных целых числа aa и bb, каждое число вводится на отдельной строке)
# и выводить наименьшее число dd, которое делится на оба этих числа без остатка.
# Sample Input 1:
#
# 1
# 2
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# 7
# 5
# Sample Output 2:
#
# 35
# Sample Input 3:
#
# 15
# 15
# Sample Output 3:
#
# 15

a = int(input())
b = int(input())
m = a
n = b
great_common_divisor = 1
while n != m and n > 1 and m > 1:
    if m % 2 == 0 and n % 2 == 0:
        m //= 2
        n //= 2
        great_common_divisor *= 2
    elif m % 2 == 0:
        m //= 2
    elif n % 2 == 0:
        n //= 2
    elif n > m:
        tmp = m
        m = (n - m) // 2
        n = tmp
    else:
        m = (m - n) // 2
if m == n:
    great_common_divisor *= n
if m == 0:
    great_common_divisor *= n
if n == 0:
    great_common_divisor *= m
least_common_multiple = a * b // great_common_divisor
print("great_common_divisor =", great_common_divisor)
print("least_common_multiple =", least_common_multiple)
