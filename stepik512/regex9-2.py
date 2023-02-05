import re
import sys


def main():
    pattern = re.compile(r'\b(\w)(\w)')
    for s in sys.stdin:
        s = s.rstrip()
        if not s:
            return
        print(re.sub(pattern, r'\2\1', s))


if __name__ == '__main__':
    main()
