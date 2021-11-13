"""
Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

Sample Input:

blabla is a tandem repetition
123123 is good too
go go
aaa


Sample Output:

blabla is a tandem repetition
123123 is good too
"""
import re
import sys


def main():
    pattern = re.compile(r'\b(\w+)\1\b')
    for line in sys.stdin:
        if line == '\n':
            return
        line = line.strip()
        if pattern.search(line):
            print(line)


if __name__ == '__main__':
    main()
