"""
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z" между которыми ровно три символа.
Sample Input:

zabcz
zzz
zzxzz
zz
zxz
zzxzxxz


Sample Output:

zabcz
zzxzz
"""
import re
import sys


def main():
    pattern = re.compile(r'z.{3}z')
    for line in sys.stdin:
        if line == '\n':
            return
        line = line.strip()
        if pattern.search(line):
            print(line)


if __name__ == '__main__':
    main()
