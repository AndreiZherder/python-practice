"""
Не используя интерпретатор, отметьте все однозначно неправильные утверждения
о содержимом переменных после выполнения этого кода:

dict1 = dict(zip(('a', 'b', 'c'), (1, 2, 3)))
range5 = list(range(5))
lst1 = [i
        for i in range5
        if i in dict1]
dict2 = {i: i*i for i in range5}
lst2 = [dict1[value] for value in dict1]
lst3 = [i
        for i in range5
        if i in lst2]

range5: [1, 2, 3, 4, 5]
dict1: ValueError
dict2: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
lst2: ['a', 'c', 'b']
lst3: ['a', 'c', 'b']
dict1: {'a': 1, 'c': 3, 'b': 2}
dict1: TypeError
lst2: []
range5: TypeError
lst2: [1, 3, 2]
lst3: [1, 2, 3]
dict2: {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
range5: [1, 2, 3, 4]
range5: [0, 1, 2, 3, 4]
lst1: []
"""


def main():
    dict1 = dict(zip(('a', 'b', 'c'), (1, 2, 3)))
    range5 = list(range(5))
    lst1 = [i
            for i in range5
            if i in dict1]
    dict2 = {i: i * i for i in range5}
    lst2 = [dict1[value] for value in dict1]
    lst3 = [i
            for i in range5
            if i in lst2]

    print(range5)
    print(dict1)
    print(dict2)
    print(lst1)
    print(lst2)
    print(lst3)


if __name__ == '__main__':
    main()
