"""
Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.

Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba",
после выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s.

Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a.
Если операций потребуется более 1000, выведите Impossible.

Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a,
или Impossible, если операций потребуется более 1000.

Условие задачи было изменено 12.09.2018
Sample Input 1:
ababa
a
b
Sample Output 1:
1
Sample Input 2:
ababa
b
a
Sample Output 2:
1
Sample Input 3:
ababa
c
c
Sample Output 3:
0
Sample Input 4:
ababac
c
c
Sample Output 4:
Impossible
"""


def solution(s: str, a: str, b: str) -> int:
    if a not in s:
        return 0
    if a in s and a in b:
        return -1
    i = 0
    old = s
    new = old.replace(a, b)
    while new != old:
        i += 1
        if i > 1000:
            return -1
        old = new
        new = old.replace(a, b)
    return i


s, a, b = (input() for _ in range(3))
ans = solution(s, a, b)
print(ans if ans >= 0 else 'Impossible')
