# TODO Список строк
#
# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая создает из указанных строк список и выводит его.
#
# Формат входных данных
# На вход программе подаются натуральное число n, а затем n строк, каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести список состоящий из указанных строк.

num, mass = int(input()), list()
for i in range(num):
    mass.append(input())
print(mass)
