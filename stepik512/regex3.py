"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.

Примечание:
Для работы со словами используйте группы символов \b и \B.
Описание этих групп вы можете найти в документации.
Sample Input:

cat
catapult and cat
catcat
concat
Cat
"cat"
!cat?


Sample Output:

cat
catapult and cat
"cat"
!cat?
"""
import re
import sys


def main():
    pattern = re.compile(r'\bcat\b')
    for line in sys.stdin:
        if line == '\n':
            return
        line = line.strip()
        if pattern.search(line):
            print(line)


if __name__ == '__main__':
    main()
