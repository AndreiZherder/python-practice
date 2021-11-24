"""
Напишите программу, которая выводит число в стиле LCD калькулятора.

На вход программе подаётся последовательность цифр, которую нужно вывести на экран в специальном стиле (см. пример).

Размер всех цифр 4 символа в ширину и 7 символов в высоту. Между цифрами в выводе должен быть один пустой столбец. Перед первой цифрой не должно быть пробелов.

Выведенные цифры должны быть обведены рамочкой, в углах которой находится символ x ("икс"), горизонтальная линия создаётся из символа - ("дефис"), а вертикальная -- из символа вертикальной черты: |.

Формат ввода:
Строка произвольной длины (минимум один символ), содержащая последовательность цифр.

Формат вывода:
9 строк, содержащих цифры, записанные в указанном в задании формате.

Sample Input:

0123456789
Sample Output:

x-------------------------------------------------x
| --        --   --        --   --   --   --   -- |
||  |    |    |    | |  | |    |       | |  | |  ||
||  |    |    |    | |  | |    |       | |  | |  ||
|           --   --   --   --   --        --   -- |
||  |    | |       |    |    | |  |    | |  |    ||
||  |    | |       |    |    | |  |    | |  |    ||
| --        --   --        --   --        --   -- |
x-------------------------------------------------x
"""
from typing import List


def rotate_clockwise(a: List[str], start_col: int, end_col: int) -> List[str]:
    n = len(a)
    return [''.join([a[i][j] for i in range(n - 1, -1, -1)]) for j in range(start_col, end_col)]


def rotate_counterclockwise(a: List[str]) -> List[str]:
    n = len(a)
    m = len(a[0])
    return [''.join([a[i][j] for i in range(n)]) for j in range(m - 1, -1, -1)]


def main():
    template = [
        'x-------------------------------------------------x',
        '| --        --   --        --   --   --   --   -- |',
        '||  |    |    |    | |  | |    |       | |  | |  ||',
        '||  |    |    |    | |  | |    |       | |  | |  ||',
        '|           --   --   --   --   --        --   -- |',
        '||  |    | |       |    |    | |  |    | |  |    ||',
        '||  |    | |       |    |    | |  |    | |  |    ||',
        '| --        --   --        --   --        --   -- |',
        'x-------------------------------------------------x'
    ]
    d = {
        'border': rotate_clockwise(template, 0, 1),
        '0': rotate_clockwise(template, 1, 5),
        'space': rotate_clockwise(template, 5, 6),
        '1': rotate_clockwise(template, 6, 10),
        '2': rotate_clockwise(template, 11, 15),
        '3': rotate_clockwise(template, 16, 20),
        '4': rotate_clockwise(template, 21, 25),
        '5': rotate_clockwise(template, 26, 30),
        '6': rotate_clockwise(template, 31, 35),
        '7': rotate_clockwise(template, 36, 40),
        '8': rotate_clockwise(template, 41, 45),
        '9': rotate_clockwise(template, 46, 50)
    }
    number = input()
    rotated_lcd = d['border'].copy()
    for digit in number:
        rotated_lcd.extend(d[digit])
        rotated_lcd.extend(d['space'])
    rotated_lcd.pop()  # remove last space
    rotated_lcd.extend(d['border'])
    lcd = rotate_counterclockwise(rotated_lcd)
    for row in lcd:
        print(row)


if __name__ == '__main__':
    main()
