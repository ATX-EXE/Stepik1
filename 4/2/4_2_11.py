# TODO Красивое число 🌶️
#
# Назовем число красивым, если оно является четырехзначным
# и делится нацело на 7 или на 17. Напишите программу, определяющую,
# является ли введённое число красивым. Программа должна вывести «YES»,
# если число является красивым, или «NO» в противном случае.
#
# Формат входных данных
# На вход программе подаётся натуральное число.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

num = int(input())
if num > 999 and num < 10000 and (num % 7 == 0 or num % 17 == 0):
    print('YES')
else:
    print('NO')
