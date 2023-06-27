# TODO Все вместе
#
# Дано натуральное число. Напишите программу, которая вычисляет:
# - сумму его цифр;
# - количество цифр в нем;
# - произведение его цифр;
# - среднее арифметическое его цифр;
# - его первую цифру;
# - сумму его первой и последней цифры.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести значения указанных величин в указанном порядке.

num = int(input())
total, counter, product_of_digits, first_digit, last_digit_2 = 0, 0, 1, 0, 0
while num != 0:
    counter += 1
    last_digit = num % 10
    if counter == 1:
        last_digit_2 = last_digit
    total += last_digit
    product_of_digits *= last_digit
    first_digit = last_digit
    num = num // 10
print(total, counter, product_of_digits, total / counter, first_digit, first_digit + last_digit_2, sep='\n')
