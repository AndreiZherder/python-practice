import json

s = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": {
            "streetAddress": "Московское ш., 101, кв.101",
            "city": "Ленинград",
            "postalCode": 101101
       },
        "phoneNumbers": [
            "812 123-1234",
            "916 123-4567"
        ]
}


def main():
    j = json.dumps(s, ensure_ascii=False)
    print(j)


if __name__ == '__main__':
    main()
