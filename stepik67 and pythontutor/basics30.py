# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
# input:
# 1 7
# 2 4
# 3 2
# 4 8
# 5 6
# 6 1
# 7 3
# 8 5
# output: NO
n = 8
x = [0 for i in range(n)]
y = [0 for i in range(n)]
beat = False
ans = 'NO'
for i in range(n):
    x[i], y[i] = [int(j) for j in input().split()]
    for j in range(0, i):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            beat = True
            ans = 'YES'
            break
    if beat:
        break
print(ans)
