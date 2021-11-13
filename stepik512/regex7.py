"""
Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.

Sample Input:

I need to understand the human mind
humanity


Sample Output:

I need to understand the computer mind
computerity
"""
import re
import sys


def main():
    pattern = re.compile(r'human')
    s = 'computer'
    for line in sys.stdin:
        if line == '\n':
            return
        line = line.strip()
        line = pattern.sub(s, line)
        print(line)


if __name__ == '__main__':
    main()
