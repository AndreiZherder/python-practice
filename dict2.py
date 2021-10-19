# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
# Все слова в словаре различны.
# # Для слова из словаря, записанного в последней строке, определите его синоним.
# input:
# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye
# output:
# Bye
n = int(input())
dictionary = dict()
for i in (range(n)):
    record = input().split()
    dictionary[record[0]] = record[1]
    dictionary[record[1]] = record[0]
request = input()
print(dictionary[request])





