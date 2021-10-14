# Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
# input: 1 2 2 3 3 3
# output: 3
a = [int(i) for i in input().split()]
i = 1
ans = 1
while i < len(a):
    if a[i] != a[i - 1]:
        ans += 1
    i += 1
print(ans)

