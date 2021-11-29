"""
В римской системе счисления для обозначения чисел используются следующие символы
(справа записаны числа, которым они соответствуют в десятичной системе счисления):

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
Будем использовать вариант, в котором числа 4, 9, 40, 90, 400 и 900
записываются как вычитание из большего числа меньшего: IV, IX, XL, XC, CD и CM, соответственно.

Напишите программу, которая переводит число из римской в десятичную систему счисления.

Формат ввода:
Строка, содержащая число, закодированное в римской системе счисления. Гарантируется, что число меньше 4000.

Формат вывода:
Строка, содержащая число в десятичной системе счисления, соответствующее введённому.

Sample Input 1:

MCMLXXXIV
Sample Output 1:

1984
Sample Input 2:

IX
Sample Output 2:

9
Sample Input 3:

III
Sample Output 3:

3
"""


def main():
    dec = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    s = input()
    ans = 0
    prev = 0
    for c in s[::-1]:
        if dec[c] < prev:
            ans -= dec[c]
        else:
            ans += dec[c]
        prev = dec[c]
    print(ans)


if __name__ == '__main__':
    main()
