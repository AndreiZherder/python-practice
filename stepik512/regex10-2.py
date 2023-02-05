import re
import sys


def main():
    pattern = re.compile(r'(\w)\1+')
    for s in sys.stdin:
        s = s.rstrip()
        if not s:
            return
        print(re.sub(pattern, r'\1', s))


if __name__ == '__main__':
    main()
