"""
Вам дана в архиве (https://stepik.org/media/attachments/lesson/24465/main.zip)
файловая структура, состоящая из директорий и файлов.
Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории,
в которых есть хотя бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.

Для лучшего понимания формата задачи, ознакомьтесь с примером.
Пример архива
Пример ответа
"""
import os
import zipfile
import requests


def main():
    os.chdir('../data')
    response = requests.get('https://stepik.org/media/attachments/lesson/24465/main.zip')
    with open('main.zip', 'wb') as file:
        file.write(response.content)
    with zipfile.ZipFile('main.zip', 'r') as file:
        file.extractall()
    with open('out.txt', 'w') as file:
        for dirpath, dirnames, filenames in os.walk('main'):
            print(dirpath, dirnames, filenames)
            for filename in filenames:
                if filename.endswith('.py'):
                    file.write(f'{dirpath}\n')
                    break


if __name__ == '__main__':
    main()
