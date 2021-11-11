"""
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Sample Input 1:

abababa
aba
Sample Output 1:

3
Sample Input 2:

abababa
abc
Sample Output 2:

0
Sample Input 3:

abc
abc
Sample Output 3:

1
Sample Input 4:

aaaaa
a
Sample Output 4:

5
"""


def solution(s: str, t: str) -> int:
    count = 0
    i = s.find(t)
    while i != -1:
        count += 1
        i = s.find(t, i + 1)
    return count


s, t = (input() for _ in range(2))
ans = solution(s, t)
print(ans)
