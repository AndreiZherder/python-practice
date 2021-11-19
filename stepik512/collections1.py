import collections
import random


lst = list(random.randrange(0, 10) for i in range(50))
print(lst)
cnt = collections.Counter(lst)
print(cnt)
print(cnt.most_common(1))

d = collections.defaultdict(list)
for i in range(10):
    d[i].extend([i, i * i, i * i * i])
print(d)

q = collections.deque(lst, 3)
print(q)