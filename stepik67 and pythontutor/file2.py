# Недавно мы считали для каждого слова количество его вхождений в строку.
# Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.
#
# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
# и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
# Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
#
# В качестве ответа укажите вывод программы, а не саму программу.
# Слова, написанные в разных регистрах, считаются одинаковыми.

# Sample Input:
# abc a bCd bC AbC BC BCD bcd ABC
#
# Sample Output:
# abc 3

inf = open('data/Bible.txt', 'r')
ouf = open('data/out.txt', 'w')
word_met = dict()
for in_string in inf:
    for i in range(len(in_string) - 1, -1, -1):
        if not in_string[i].isalnum() and in_string[i] != ' ':
            in_string = in_string[:i] + in_string[i + 1:]
    in_string = in_string.strip()
    ouf.write(f'{in_string}\n')  # в добавление к задаче в файл записываются строки без служебных символов
    words = in_string.lower().split()
    for word in words:
        if word not in word_met:
            word_met[word] = 1
        else:
            word_met[word] += 1
max_times_word_met = max(word_met.values())
most_met_words = [word for word in word_met.keys() if word_met[word] == max_times_word_met]
word = min(most_met_words)
for word, times_word_met in sorted(word_met.items(), key=lambda item: (item[1], item[0])):
    ouf.write(f'{word} {times_word_met}\n')  # в добавление к задаче в файл записываютя слова и их количество
ouf.write(f'{word} {max_times_word_met}\n')
ouf.close()
inf.close()
