# TODO Сумма чисел
#
# На вход программе подается последовательность целых чисел,
# каждое число на отдельной строке. Концом последовательности
# является любое отрицательное число. Напишите программу,
# которая выводит сумму всех членов данной последовательности.
#
# Формат входных данных
# На вход программе подается последовательность чисел, каждое
# число на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести сумму членов данной последовательности.

num = int(input())
total = 0
while num >= 0:
    total += num
    num = int(input())
print(total)
