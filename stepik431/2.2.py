"""
Write a program that uses input to prompt a user for their name and then welcomes them.

Enter your name: Chuck
Hello Chuck
Для считывания значений с клавиатуры в Python 3 используется функция input.

В этой задаче ожидается использование функции input с аргументом.
"""


def main():
    print(f'Hello {input("Enter your name: ")}')


if __name__ == '__main__':
    main()
