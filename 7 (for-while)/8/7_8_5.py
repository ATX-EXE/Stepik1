# TODO Таблица-1
#
# Дано натуральное число n (n≤ 9). Напишите программу,
# которая печатает таблицу размером n×3 состоящую
# из данного числа (числа отделены одним пробелом).
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести таблицу размером n×3 состоящую из данного числа.
#
# Примечание. В конце строки может быть пробел.

num = int(input())
for i in range(num):
    for j in range(3):
        print(num, end=' ')
    print('')
