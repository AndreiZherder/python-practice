import sys, re


def main():
    pattern = re.compile(r'^.*cat.*cat.*$')
    for s in sys.stdin:
        s = s.rstrip()
        if re.match(pattern, s):
            print(s)


if __name__ == '__main__':
    main()
