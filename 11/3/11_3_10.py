# TODO Список делителей
#
# На вход программе подается натуральное число n. Напишите программу,
# которая создает список состоящий из делителей введенного числа.
#
# Формат входных данных
# На вход программе подается натуральное число n.
#
# Формат выходных данных
# Программа должна вывести список, состоящий из делителей введенного числа.

num, nums = int(input()), list()
for i in range(1, num + 1):
    if num % i == 0:
        nums.append(i)
print(nums)
