# TODO Количество пятерок
#
# На вход программе подается последовательность целых
# чисел от 1 до 5, характеризующее оценку ученика,
# каждое число на отдельной строке. Концом последовательности
# является любое отрицательное число, либо число большее 5.
# Напишите программу, которая выводит количество пятерок.
#
# Формат входных данных
# На вход программе подается последовательность чисел,
# каждое число на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести количество пятерок.

num = int(input())
total = 0
while 0 < num < 6:
    if num == 5:
        total += 1
    num = int(input())
print(total)