# TODO Вторая цифра
#
# Дано натуральное число n(n>9). Напишите программу,
# которая определяет его вторую (с начала) цифру.
#
# Формат входных данных
# На вход программе подается одно натуральное число, состоящее как минимум из двух цифр.
#
# Формат выходных данных
# Программа должна вывести его вторую (с начала) цифру.

num, second_num = int(input()), 0
while num != 0:
    last_digit = num % 10
    if num > 9:
        second_num = last_digit
    num = num // 10
print(second_num)
