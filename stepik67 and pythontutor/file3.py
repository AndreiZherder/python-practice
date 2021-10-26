# Имеется файл с данными по успеваемости абитуриентов.
# Он представляет из себя набор строк, где в каждой строке записана следующая информация:
# Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
#
# Поля внутри строки разделены точкой с запятой, оценки — целые числа.
# Напишите программу, которая считывает исходный файл с подобной структурой
# и для каждого абитуриента записывает его среднюю оценку по трём предметам на отдельной строке,
# соответствующей этому абитуриенту, в файл с ответом.
#
# Также вычислите средние баллы по математике,
# физике и русскому языку по всем абитуриентам и добавьте полученные значения, разделённые пробелом,
# последней строкой в файл с ответом.
#
# В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику
# и одной строкой со средними оценками по трём предметам.

# Sample Input:
#
# Петров;85;92;78
# Сидоров;100;88;94
# Иванов;58;72;85
#
# Sample Output:
#
# 85.0
# 94.0
# 71.666666667
# 81.0 84.0 85.666666667

grades = []
with open('data/dataset_3363_4.txt', 'r', encoding='utf-8') as inf:
    for line in inf:
        applicant = line.split(';')
        grades.append(applicant)
sum_of_math_grades = 0
sum_of_physics_grades = 0
sum_of_russian_grades = 0
with open('data/out.txt', 'w', encoding='utf-8') as ouf:
    for applicant in grades:
        sum_of_applicant_grades = 0
        for grade in applicant[1:]:
            sum_of_applicant_grades += int(grade)
        mean = sum_of_applicant_grades / (len(applicant) - 1)
        ouf.write(f'{mean}\n')
        sum_of_math_grades += int(applicant[1])
        sum_of_physics_grades += int(applicant[2])
        sum_of_russian_grades += int(applicant[3])
    mean_of_math_grades = sum_of_math_grades / len(grades)
    mean_of_physics_grades = sum_of_physics_grades / len(grades)
    mean_of_russian_grades = sum_of_russian_grades / len(grades)
    ouf.write(f'{mean_of_math_grades} {mean_of_physics_grades} {mean_of_russian_grades}\n')
