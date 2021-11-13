import re
pattern = re.compile(r'\b[А-Я]+\b')
with open('../data/text.txt', 'r', encoding='utf8') as input_file:
    text = input_file.read()

res = pattern.match(text)
print('pattern.match(text) = ', res)
res = pattern.search(text)
print('pattern.search(text) = ', res)
res = pattern.findall(text)
print('pattern.findall(text) = ', res)
