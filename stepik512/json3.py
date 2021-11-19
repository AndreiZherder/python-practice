"""
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел.
Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

Пример выходного файла:
Interesting
Boring
Interesting
Boring

У вас есть неограниченное число попыток.
Время одной попытки: 5 mins
"""
import json
import requests


def main():
    with open('../data/dataset_24476_3.txt', 'r') as input_file, open('../data/out.txt', 'w') as output_file:
        for num in input_file:
            url = f'http://numbersapi.com/{num.strip()}/math?json'
            resp = requests.get(url)
            print(resp.url)
            print(resp.status_code)
            print(resp.json())
            output_file.write('Interesting\n' if resp.json()['found'] else 'Boring\n')


if __name__ == '__main__':
    main()
