"""
Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.
Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории,
в которых есть хотя бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.

Для лучшего понимания формата задачи, ознакомьтесь с примером.
Пример архива
Пример ответа
"""
import os
import shutil
import requests
import zipfile


os.chdir('../data')
response = requests.get('https://stepik.org/media/attachments/lesson/24465/main.zip', stream=True)
with open('main.zip', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response
with zipfile.ZipFile('main.zip', 'r') as main_zip:
    main_zip.extractall()
with open('out.txt', 'w') as out_file:
    for root, subdirs, files in os.walk('main'):
        for file in files:
            if file.endswith('.py'):
                out_file.write(f'{root}\n')
                break

