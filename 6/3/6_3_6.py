# TODO Пол и потолок
#
# Напишите программу, вычисляющую значение ⌈x⌉ +⌊x⌋ по заданному вещественному числу x.
#
# Формат входных данных
# На вход программе подается одно вещественное число x.
#
# Формат выходных данных
# Программа должна вывести одно число – значение указанного выражения.
#
# Примечание. ⌈x⌉ – потолок числа, ⌊x⌋ – пол числа.

from math import ceil, floor

x = float(input())
print(ceil(x) + floor(x))
