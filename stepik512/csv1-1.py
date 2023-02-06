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
import csv
from collections import Counter


def main():
    with open('../data/Crimes.csv', 'r') as file:
        records = csv.DictReader(file)
        cnt = Counter()
        for record in filter(lambda x: x['Date'][6:10] == '2015', records):
            cnt[record['Primary Type']] += 1
    print(max(cnt, key=cnt.get))


if __name__ == '__main__':
    main()
