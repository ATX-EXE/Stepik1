# TODO Четырёхзначное число
#
# Напишите программу для нахождения цифр четырёхзначного числа.
#
# Формат входных данных
# На вход программе подаётся положительное четырёхзначное целое число.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

num = int(input())
num_d = num % 10
num_c = (num % 100) // 10
num_b = (num % 1000) // 100
num_a = num // 1000
print('Цифра в позиции тысяч равна', num_a)
print('Цифра в позиции сотен равна', num_b)
print('Цифра в позиции десятков равна', num_c)
print('Цифра в позиции единиц равна', num_d)
