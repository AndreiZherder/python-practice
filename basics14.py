# Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты
# группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.
#
# Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на
# этот символ и количество его повторений в этой позиции строки.
#
# Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом
# и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.
s = input() + "."
ch = s[0]
count = 1
ans = ""
for i in range(1, len(s)):
    if s[i] == ch:
        count += 1
    else:
        ans += ch + str(count)
        ch = s[i]
        count = 1
print(ans)