# TODO Сумма факториалов
#
# Дано натуральное число n. Напишите программу, которая выводит значение суммы 1!+2!+3!+…+n!.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести значение суммы 1!+2!+3!+…+n!.
#
# Примечание 1. Факториалом натурального числа n, называется произведение
# всех натуральных чисел от 1 до n, то есть n!=1⋅2⋅3⋅…⋅n
#
# Примечание 2. Задачу можно решить без вложенного цикла. Напишите две версии программы =)

import math

num = int(input())
total = 0
for i in range(1, num + 1):
    total += math.factorial(i)
print(total)
