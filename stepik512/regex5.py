"""
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\".
Sample Input:

\w denotes word character
No slashes here


Sample Output:

\w denotes word character
"""
import re
import sys


def main():
    pattern = re.compile(r'\\')
    for line in sys.stdin:
        if line == '\n':
            return
        line = line.strip()
        if pattern.search(line):
            print(line)


if __name__ == '__main__':
    main()
