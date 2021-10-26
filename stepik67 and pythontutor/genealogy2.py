# Даны два элемента в дереве. Определите, является ли один из них потомком другого.
#
# Во входных данных записано дерево в том же формате, что и в предыдущей задаче Далее идет число запросов K.
# В каждой из следующих K строк, содержатся имена двух элементов дерева.
#
# Для каждого такого запроса выведите одно из трех чисел: 1, если первый элемент является предком второго,
# 2, если второй является предком первого или 0, если ни один из них не является предком другого.
# Input:
# 9
# Alexei Peter_I
# Anna Peter_I
# Elizabeth Peter_I
# Peter_II Alexei
# Peter_III Anna
# Paul_I Peter_III
# Alexander_I Paul_I
# Nicholaus_I Paul_I
# 3
# Anna Nicholaus_I
# Peter_II Peter_I
# Alexei Paul_I
#
# Output:
# 1 2 0
def is_ancestor(tree: dict, parent: str, child: str):
    res = False
    while tree[child]['parent'] is not None:
        if tree[child]['parent'] == parent:
            res = True
            break
        else:
            child = tree[child]['parent']
    return res


n = int(input())
tree = {}
for i in range(n - 1):
    child, parent = input().split()
    if parent in tree:
        tree[parent]['children'].append(child)
    else:
        tree[parent] = {'height': 0, 'parent': None, 'children': [child]}
    if child in tree:
        tree[child]['parent'] = parent
    else:
        tree[child] = {'height': 0, 'parent': parent, 'children': []}
n = int(input())
for i in range(n):
    person1, person2 = input().split()
    if is_ancestor(tree, person1, person2):
        print('1', end=' ')
    elif is_ancestor(tree, person2, person1):
        print('2', end=' ')
    else:
        print('0', end=' ')
