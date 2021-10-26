# В генеалогическом древе определите для двух элементов их наименьшего общего предка (Lowest Common Ancestor).
# Наименьшим общим предком элементов A и B является такой элемент C, что С является предком A, C является предком B,
# при этом глубина C является наибольшей из возможных. При этом элемент считается своим собственным предком.
#
# Формат входных данных аналогичен предыдущей задаче
#
# Для каждого запроса выведите наименьшего общего предка данных элементов.
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
# Alexander_I Nicholaus_I
# Peter_II Paul_I
# Alexander_I Anna
#
# Output:
# Paul_I
# Peter_I
# Anna

def ancestors(tree: dict, child: str):
    res = [child]
    while tree[child]['parent'] is not None:
        res.append(tree[child]['parent'])
        child = tree[child]['parent']
    return res


def lowest_common_ancestor(tree: dict, child1: str, child2: str):
    child_1_ancestors = ancestors(tree, child1)
    if child2 in child_1_ancestors:
        return child2
    while tree[child2]['parent'] is not None:
        if tree[child2]['parent'] in child_1_ancestors:
            return tree[child2]['parent']
        child2 = tree[child2]['parent']


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
    child1, child2 = input().split()
    print(lowest_common_ancestor(tree, child1, child2))
