# В файловую систему одного суперкомпьютера проник вирус, который сломал контроль за правами доступа к файлам.
# Для каждого файла известно, с какими действиями можно к нему обращаться:
# запись W,
# чтение R,
# запуск X.
# В первой строке содержится число N — количество файлов содержащихся в данной файловой системе.
# В следующих N строчках содержатся имена файлов и допустимых с ними операций, разделенные пробелами.
# Далее указано чиcло M — количество запросов к файлам. В последних M строках указан запрос вида Операция Файл.
# К одному и тому же файлу может быть применено любое колличество запросов.
#
# Вам требуется восстановить контроль над правами доступа к файлам
# (ваша программа для каждого запроса должна будет возвращать OK если над файлом выполняется допустимая операция,
# или же Access denied, если операция недопустима.
# input:
# 4
# helloworld.exe R X
# pinglog W R
# nya R
# goodluck X W R
# 5
# read nya
# write helloworld.exe
# execute nya
# read pinglog
# write pinglog
# output:
# OK
# Access denied
# Access denied
# OK
# OK
masks = {'R': 0x4, 'W': 0x2, 'X': 0x1, 'read': 0x4, 'write': 0x2, 'execute': 0x1}
files = dict()
for i in range(int(input())):
    file_params = input().split()
    file_name = file_params[0]
    rights = 0
    for j in range(1, len(file_params)):
        rights |= masks[file_params[j]]
    files[file_name] = rights
for i in range(int(input())):
    operation, file_name = input().split()
    if files[file_name] & masks[operation] > 0:
        print('OK')
    else:
        print('Access denied')
