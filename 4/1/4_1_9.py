# TODO Наименьшее из двух чисел
#
# Напишите программу, которая определяет наименьшее из двух чисел.
#
# Формат входных данных
# На вход программе подаётся два различных целых числа.
#
# Формат выходных данных
# Программа должна вывести наименьшее из двух чисел.

num_1, num_2 = int(input()), int(input())
if num_1 < num_2:
    print(num_1)
else:
    print(num_2)