"""
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
Sample Input:

attraction
buzzzz


Sample Output:

atraction
buz
"""
import re
import sys


def main():
    pattern = re.compile(r'(\w)(\1)+')
    s = 'argh'
    for line in sys.stdin:
        if line == '\n':
            return
        line = line.strip()
        line = pattern.sub(r'\1', line)
        print(line)


if __name__ == '__main__':
    main()
