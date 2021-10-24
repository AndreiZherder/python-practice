# Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
# Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита,
# на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом,
# и ещё одна строка, которую нужно расшифровать.
# Sample Input 1:
#
# abcd
# *d%#
# abacabadaba
# #*%*d*%
# Sample Output 1:
#
# *d*%*d*#*d*
# dacabac
code_str, decode_str = input(), input()
code = dict(zip(code_str, decode_str))
decode = dict(zip(decode_str, code_str))
str1, str2 = input(), input()
ans1 = ''.join((code[ch] for ch in str1))
ans2 = ''.join((decode[ch] for ch in str2))
print(ans1)
print(ans2)
