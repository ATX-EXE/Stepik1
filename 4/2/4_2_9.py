# TODO Принадлежность 2
#
# Напишите программу, которая принимает целое число x и определяет,
# принадлежит ли данное число указанным промежуткам.
#
# Формат входных данных
# На вход программе подаётся целое число x.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

num = int(input())
if num <= -3 or 7 <= num:
    print('Принадлежит')
else:
    print('Не принадлежит')
