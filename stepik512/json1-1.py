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
from collections import defaultdict
from typing import Set


def main():
    def dfs(root: str) -> Set[str]:
        if root not in tree:
            memo[root] = {root}
        elif root not in memo:
            memo[root] = {root}
            for child in tree[root]:
                memo[root] |= dfs(child)
        return memo[root]

    tree = defaultdict(list)
    for d in json.loads(input()):
        for node in d['parents']:
            tree[node].append(d['name'])
    memo = {}
    for node in tree:
        dfs(node)
    for k, v in sorted(memo.items()):
        print(f'{k} : {len(v)}')


if __name__ == '__main__':
    main()
