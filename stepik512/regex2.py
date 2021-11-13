"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

Примечание:
Считать все строки по одной из стандартного потока ввода вы можете, например, так

import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line

Sample Input:

catcat
cat and cat
catac
cat
ccaatt


Sample Output:

catcat
cat and cat
"""
import re
import sys


def main():
    pattern = re.compile(r'cat.*cat')
    for line in sys.stdin:
        if line == '\n':
            return
        line = line.strip()
        if pattern.search(line):
            print(line)


if __name__ == '__main__':
    main()
