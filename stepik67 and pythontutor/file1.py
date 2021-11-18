# Напишите программу, которая считывает из файла строку, соответствующую тексту,
# сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

# Sample Input:
# a3b4c2e10b1
#
# Sample Output:
# aaabbbbcceeeeeeeeeeb

inf = open('../data/dataset_3363_2.txt', 'r')
ouf = open('../data/out.txt', 'w')
for in_string in inf:
    in_string = in_string.strip()
    out_string = ''
    alpha = ''
    alpha_count = ''
    for ch in in_string:
        if ch.isalpha():
            out_string += alpha * (0 if alpha_count == '' else int(alpha_count))
            alpha = ch
            alpha_count = ''
        elif ch.isdigit():
            alpha_count += ch
    out_string += alpha * int(alpha_count)
    ouf.write(out_string + '\n')
ouf.close()
inf.close()
