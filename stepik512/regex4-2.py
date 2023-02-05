import re
import sys


def main():
    pattern = re.compile(r'z.{3}z')
    for s in sys.stdin:
        s = s.rstrip()
        if not s:
            return
        if re.search(pattern, s):
            print(s)


if __name__ == '__main__':
    main()
