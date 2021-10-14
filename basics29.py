# N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N.
# Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri включительно.
# Определите, какие кегли остались стоять на месте.
# Программа получает на вход количество кеглей N и количество бросков K.
# Далее идет K пар чисел li, ri, при этом 1≤ li≤ ri≤ N.
#
# Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я кегля осталась стоять,
# или “.”, если j-я кегля была сбита.
# input:
# 10 3
# 8 10
# 2 5
# 3 6
# output: I.....I...
N, K = [int(i) for i in input().split()]
I = ['I' for i in range(N)]
for i in range(K):
    li, ri = [int(j) for j in input().split()]
    I[li - 1:ri] = ['.' for j in range(li - 1, ri)]
print(''.join(I))
