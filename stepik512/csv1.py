"""
Вам дана частичная выборка из датасета зафиксированных преступлений,
совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv
https://stepik.org/media/attachments/lesson/24473/Crimes.csv

Yes
"""
import requests
import csv
import datetime


def main():
    resp = requests.get('https://stepik.org/media/attachments/lesson/24473/Crimes.csv')
    with open('../data/Crimes.csv', 'w+', newline='') as f:
        f.write(resp.text)
        f.seek(0)
        reader = csv.DictReader(f)
        types = dict()
        for row in reader:
            if datetime.datetime.strptime(row['Date'], '%m/%d/%Y %H:%M:%S %p').year == 2015:
                types[row['Primary Type']] = types.get(row['Primary Type'], 0) + 1
        print(max(types.items(), key=lambda item: item[1]))


if __name__ == '__main__':
    main()
