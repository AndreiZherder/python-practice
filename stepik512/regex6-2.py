import re
import sys


def main():
    pattern = re.compile(r'\b(\w+)(\1)\b')
    for s in sys.stdin:
        s = s.rstrip()
        if not s:
            return
        if re.search(pattern, s):
            print(s)


if __name__ == '__main__':
    main()
