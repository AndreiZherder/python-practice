import re
import sys


def main():
    pattern = re.compile(r'human')
    for s in sys.stdin:
        s = s.rstrip()
        if not s:
            return
        print(re.sub(pattern, 'computer', s))


if __name__ == '__main__':
    main()
