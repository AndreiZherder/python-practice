"""
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
а чётные нацело делит на два.
Функция не должна ничего возвращать, требуется только изменение переданного списка, например:

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
Также функция не должна осуществлять ввод/вывод информации.
"""
from typing import List


def modify_list(l: List[int]):
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 == 1:
            del l[i]
        else:
            l[i] //= 2


def main():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    modify_list(l)
    print(l)


if __name__ == '__main__':
    main()
