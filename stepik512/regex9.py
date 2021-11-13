"""
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.
Sample Input:

this is a text
"this' !is. ?n1ce,


Sample Output:

htis si a etxt
"htis' !si. ?1nce,
"""
import re
import sys


def main():
    pattern = re.compile(r'\b(\w)(\w)')
    s = 'argh'
    for line in sys.stdin:
        if line == '\n':
            return
        line = line.strip()
        line = pattern.sub(r'\2\1', line)
        print(line)


if __name__ == '__main__':
    main()
