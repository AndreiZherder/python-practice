"""
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам.
У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents,
которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно,
и что никакой класс не наследуется явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Sample Output:

A : 3
B : 1
C : 2
"""
import json


def dfs(tree: dict, parent: str) -> set:
    children = tree.get(parent, [])
    descendants = set(children)
    for child in children:
        descendants |= dfs(tree, child)
    descendants.add(parent)
    return descendants


def main():
    children = json.loads(input())
    tree = dict()
    for child in children:
        if child['name'] not in tree:
            tree[child['name']] = []
        for parent in child['parents']:
            tree[parent] = tree.get(parent, []) + [child['name']]
    for parent in sorted(tree):
        descendants = dfs(tree, parent)
        print(f'{parent} : {len(descendants)}')


if __name__ == '__main__':
    main()
