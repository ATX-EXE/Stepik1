# TODO Абсолютная сумма
#
# Даны пять чисел a1, a2, a3, a4, a5. Напишите программу, которая вычисляет сумму их модулей
# |a1| + |a2| + |a3| + |a4| + |a5|.
#
# Формат входных данных
# На вход программе подается пять действительных чисел
# a1, a2, a3, a4, a5, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести одно число – сумму модулей введённых чисел.

num_1, num_2, num_3, num_4, num_5 = float(input()), float(input()), float(input()), float(input()), float(input())
print(abs(num_1) + abs(num_2) + abs(num_3) + abs(num_4) + abs(num_5))