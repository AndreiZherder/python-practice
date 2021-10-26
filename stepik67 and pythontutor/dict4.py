# Дан текст: в первой строке задано число строк, далее идут сами строки.
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
# input:
# 1
# apple orange banana banana orange
# output:
# banana
words = dict()
for i in (range(int(input()))):
    request = input().split()
    for word in request:
        words[word] = words.get(word, 0) + 1
ans = sorted(words.items(), key=lambda x: (-x[1], x[0]))
print(ans[0][0])
