# Дана база данных о продажах некоторого интернет-магазина.
# Каждая строка входного файла представляет собой запись вида Покупатель товар количество,
# где Покупатель — имя покупателя (строка без пробелов), товар — название товара (строка без пробелов),
# количество — количество приобретенных единиц товара.
#
# Создайте список всех покупателей,
# а для каждого покупателя подсчитайте количество приобретенных им единиц каждого вида товаров.
# Список покупателей, а также список товаров для каждого покупателя нужно выводить в лексикографическом порядке.
# Sample Input1:
#
# Ivanov paper 10
# Petrov pens 5
# Ivanov marker 3
# Ivanov paper 7
# Petrov envelope 20
# Ivanov envelope 5

# Sample Output1:
#
# Ivanov:
# envelope 5
# marker 3
# paper 17
# Petrov:
# envelope 20
# pens 5
from sys import stdin
customers = dict()
products = dict()
for line in stdin.readlines():
    input_list = line.split()
    customer = input_list[0]
    product = input_list[1]
    quantity = int(input_list[2])
    if customer in customers:
        if product in customers[customer]:
            customers[customer][product] += quantity
        else:
            customers[customer][product] = quantity
    else:
        customers[customer] = {product: quantity}

for customer, products in sorted(customers.items()):
    print(customer + ':')
    for product, quantity in sorted(products.items()):
        print(product, quantity, sep=' ')
