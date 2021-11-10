"""
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

Пример выходного файла:
ff
dde
c
ab
"""
with open('../data/in.txt', 'r', encoding='utf8') as inf,\
        open('../data/out.txt', 'w', encoding='utf8') as ouf:
    lines = inf.readlines()
    while lines:
        ouf.write(lines.pop())

