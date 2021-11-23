"""
What will the following Python 3 program print out?

def fred():
    print("Zap")

def jane():
    print("ABC")

jane()
fred()
jane()
"""


def main():
    def fred():
        print("Zap")

    def jane():
        print("ABC")

    jane()
    fred()
    jane()


if __name__ == '__main__':
    main()
