"""
На вход программе подаётся строка, содержащая слова, разделённые пробелом.
Программа должна вывести статистику длин слов в полученной строке, от меньшей длины слова к большей (см. пример).

Словом считается последовательность произвольных символов, окружённая пробелами либо границами строки.
Заметьте, что знаки препинания также относятся к слову.

Формат ввода:
Одна строка, содержащая последовательности латинских символов и знаков препинания, разделённые пробелом.

Формат вывода:
Для каждой длины слова, встречающейся в исходной строке, нужно указать количество слов с такой длиной
длина: количество
Статистика должна выводиться в порядке увеличения длины.

Sample Input:

Beautiful is better than ugly. Explicit is better than implicit.
Sample Output:

2: 2
4: 2
5: 1
6: 2
8: 1
9: 2
"""
import collections


def main():
    cnt = collections.Counter([len(word) for word in input().split()])
    for k, v in sorted(cnt.items()):
        print(f'{k}: {v}')


if __name__ == '__main__':
    main()