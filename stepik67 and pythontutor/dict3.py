# Как известно, в США президент выбирается не прямым голосованием, а путем двухуровневого голосования.
# Сначала проводятся выборы в каждом штате и определяется победитель выборов в данном штате.
# Затем проводятся государственные выборы:
# на этих выборах каждый штат имеет определенное число голосов — число выборщиков от этого штата.
# На практике, все выборщики от штата голосуют в соответствии с результами голосования внутри штата,
# то есть на заключительной стадии выборов в голосовании участвуют штаты, имеющие различное число голосов.
#
# В первой строке дано количество записей.
# Далее, каждая запись содержит фамилию кандидата и число голосов, отданных за него в одном из штатов.
# Подведите итоги выборов: для каждого из участника голосования определите число отданных за него голосов.
# Участников нужно выводить в алфавитном порядке.
# input:
# 5
# McCain 10
# McCain 5
# Obama 9
# Obama 8
# McCain 1
# output:
# McCain 16
# Obama 17
dictionary = dict()
for i in (range(int(input()))):
    candidate, votes = input().split()
    dictionary[candidate] = dictionary.get(candidate, 0) + int(votes)
for candidate, votes in sorted(dictionary.items()):
    print(candidate, votes)





