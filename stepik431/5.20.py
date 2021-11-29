"""
Напишите программу, вычисляющую следующее состояние поля для Game of life.

Поле представляет собой прямоугольник, причём для крайних клеток поля соседними являются клетки с противоположного конца
(поле представляет собой тор).

Формат ввода:

На первой строке указаны два целых числа через пробел -- высота и ширина поля.
В следующих строках подаётся состояние поля. Точка "." обозначает мёртвую клетку, символ "X" − живую.

Формат вывода:
Следующее состояние поля, используя те же обозначения, что использовались на вводе.

Sample Input 1:

5 5
.....
..X..
...X.
.XXX.
.....
Sample Output 1:

.....
.....
.X.X.
..XX.
..X..
Sample Input 2:

5 5
.....
.....
.XXX.
.....
.....
Sample Output 2:

.....
..X..
..X..
..X..
.....
Sample Input 3:

5 6
...XX.
.XX...
..X...
XX....
X..XX.
Sample Output 3:

.X..XX
.XX...
X.X...
XXXX.X
XXXXX.
"""
from typing import List


def alive_neighbors(field: List[List[str]], i: int, j: int) -> int:
    n = len(field)
    m = len(field[0])
    k = 0
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]
    for neighbor in range(8):
        if field[(i + di[neighbor]) % n][(j + dj[neighbor]) % m] == 'X':
            k += 1
    return k


def main():
    n, m = (int(_) for _ in input().split())
    field = [[c for c in input()] for i in range(n)]
    next_field = [['.' for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            k = alive_neighbors(field, i, j)
            if field[i][j] == '.' and k == 3:
                next_field[i][j] = 'X'
            if field[i][j] == 'X':
                if k in [2, 3]:
                    next_field[i][j] = 'X'
                else:
                    next_field[i][j] = '.'
    for i in range(n):
        print(''.join(next_field[i]))


if __name__ == '__main__':
    main()
