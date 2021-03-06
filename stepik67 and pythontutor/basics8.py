# Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался.
# Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
#
# Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу,
# которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.
#
# На вход программе подаётся строка из шести цифр.
# # Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.
#
# Sample Input 1:
#
# 090234
# Sample Output 1:
#
# Счастливый
# Sample Input 2:
#
# 123456
# Sample Output 2:
#
# Обычный

n = int(input())
s1 = n // 100000 + n % 100000 // 10000 + n % 10000 // 1000
s2 = n % 1000 // 100 + n % 100 // 10 + n % 10
if s1 == s2:
    print("Счастливый")
else:
    print("Обычный")
