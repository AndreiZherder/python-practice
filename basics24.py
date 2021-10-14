# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
# input: 3 4 5 2 1
# output: 3 4 1 2 5
a = [int(i) for i in input().split()]
max = max(a)
pos_max = a.index(max)
min = min(a)
pos_min = a.index(min)
a[pos_min], a[pos_max] = a[pos_max], a[pos_min]
print(' '.join(str(i) for i in a))
