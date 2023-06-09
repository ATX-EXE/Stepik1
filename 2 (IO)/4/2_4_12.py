# TODO Арифметическая прогрессия
#
# Арифметической прогрессией называется последовательность чисел a1, a2 .. an,
# каждое из которых, начиная с a2, получается из предыдущего прибавлением
# к нему одного и того же постоянного числа d (разность прогрессии), то есть:
# An = An-1 + d
# Если известен первый член прогрессии и её разность, то n-ый член
# арифметической прогрессии находится по формуле:
# An = A1 + D(n-1)
#
# Входные данные
# На вход программе подаётся три целых числа: a1, d, n, каждое на отдельной строке.
#
# Выходные данные
# Программа должна вывести n-ый член арифметической прогрессии.

num, num_d, num_n = int(input()), int(input()), int(input())
print(num + (num_d * (num_n - 1)))
