# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
# Загрузите содержимое последнего файла из набора, как ответ на это задание.

import requests
DEFAULT_ADDRESS = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('./data/dataset_3378_3.txt', 'r', encoding='utf-8') as inf:
    url = inf.readline().strip()
next_file_exists = True
while next_file_exists:
    ans = requests.get(url)
    text = ans.text
    print(text)
    if text.split()[0] == 'We':
        next_file_exists = False
        with open('./data/out.txt', 'w', encoding='utf-8') as ouf:
            ouf.write(text)
    else:
        url = DEFAULT_ADDRESS + text
