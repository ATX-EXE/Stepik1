# TODO Dog age
#
# На вход программе подается число n – количество собачьих лет.
# Напишите программу, которая вычисляет возраст собаки в человеческих годах.
#
# Формат входных данных
# На вход программе подаётся натуральное число – количество собачьих лет.
#
# Формат выходных данных
# Программа должна вывести возраст собаки в человеческих годах.
#
# Примечание. В течение первых двух лет собачий год равен 10.5 человеческим годам.
# После этого каждый год собаки равен 4 человеческим годам.

num = float(input())
if 0 <= num <= 2:
    print(num * 10.5)
else:
    print((num - 2) * 4 + 2 * 10.5)
