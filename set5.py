# Каждый из некоторого множества школьников некоторой школы знает некоторое количество языков.
# Нужно определить сколько языков знают все школьники, и сколько языков знает хотя бы один из школьников.
#
# В первой строке задано количество школьников.
# Для каждого из школьников сперва записано количество языков,
# которое он знает, а затем - названия языков, по одному в строке.
#
# В первой строке выведите количество языков, которые знают все школьники.
# Начиная со второй строки - список таких языков. Затем - количество языков, которые знает хотя бы один школьник,
# на следующих строках - список таких языков. Языки нужно выводить в лексикографическом порядке, по одному на строке.
# input:
# 3
# 3
# Russian
# English
# Japanese
# 2
# Russian
# English
# 1
# English
#
# output:
# 1
# English
# 3
# English
# Japanese
# Russian
def print_info_about_set(s):
    print(len(s))
    print(*sorted(s), sep='\n')


kids_number = int(input())
kids = []
all_languages = set()
for i in range(kids_number):
    languages_number = int(input())
    languages = set()
    for j in range(languages_number):
        languages.add(input())
        all_languages |= languages
    kids.append(languages)
languages_known_by_all = all_languages
languages_known_by_at_least_one = set()
for languages_known_by_kid in kids:
    languages_known_by_all &= languages_known_by_kid
    languages_known_by_at_least_one |= languages_known_by_kid
print_info_about_set(languages_known_by_all)
print_info_about_set(languages_known_by_at_least_one)
