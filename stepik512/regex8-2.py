import re
import sys


def main():
    pattern = re.compile(r'\b[Aa]+\b')
    for s in sys.stdin:
        s = s.rstrip()
        if not s:
            return
        print(re.sub(pattern, 'argh', s, count=1))


if __name__ == '__main__':
    main()
