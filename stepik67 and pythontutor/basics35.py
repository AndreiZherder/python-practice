# Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали,
# выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
# input:
# 5
# output:
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9
n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
nn = n * n
step = 1
i = 0
j = 0
while step <= nn:
    while step <= nn and j < n and a[i][j] == 0:
        a[i][j] = step
        j += 1
        step += 1
    j -= 1
    i += 1
    while step <= nn and i < n and a[i][j] == 0:
        a[i][j] = step
        i += 1
        step += 1
    i -= 1
    j -= 1
    while step <= nn and j >= 0 and a[i][j] == 0:
        a[i][j] = step
        j -= 1
        step += 1
    j += 1
    i -= 1
    while step <= nn and i >= 0 and a[i][j] == 0:
        a[i][j] = step
        i -= 1
        step += 1
    j += 1
    i += 1
for now in a:
    print(*now)
