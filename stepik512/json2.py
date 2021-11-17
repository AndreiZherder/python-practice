import json

s = '{' \
    '    "firstName": "Иван",' \
    '    "lastName": "Иванов",' \
    '    "address": {' \
    '        "streetAddress": "Московское ш., 101, кв.101",' \
    '        "city": "Ленинград",' \
    '        "postalCode": 101101' \
    '    },' \
    '    "phoneNumbers": [' \
    '        "812 123-1234",' \
    '        "916 123-4567"' \
    '    ]' \
    '}'


def main():
    j = json.loads(s)
    for k, v in j.items():
        print(f'{k}: {v}')


if __name__ == '__main__':
    main()
