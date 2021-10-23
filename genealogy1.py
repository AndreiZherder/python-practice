# В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
# Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой.
# У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.
# Вам дано генеалогическое древо, определите высоту всех его элементов.
# Программа получает на вход число элементов в генеалогическом древе N.
# Далее следует N−1 строка, задающие родителя для каждого элемента древа, кроме родоначальника.
# Каждая строка имеет вид имя_потомка имя_родителя.
#
# Программа должна вывести список всех элементов древа в лексикографическом порядке.
# После вывода имени каждого элемента необходимо вывести его высоту.
# Примечание
# Эта задача имеет решение сложности O(n),
# но вам достаточно написать решение сложности O(n2) (не считая сложности обращения к элементам словаря).
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
#
# Output:
# Alexander_I 4
# Alexei 1
# Anna 1
# Elizabeth 1
# Nicholaus_I 4
# Paul_I 3
# Peter_I 0
# Peter_II 2
# Peter_III 2

def calculate_child_heights(tree: dict, parent: str):
    for child in tree[parent]['children']:
        tree[child]['height'] = tree[parent]['height'] + 1
        calculate_child_heights(tree, child)


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
ancestor = [k for k, v in tree.items() if v['parent'] is None][0]
calculate_child_heights(tree, ancestor)
for person in sorted(tree):
    print(person, tree[person]['height'])
