# TODO Одинаковые цифры
#
# Дано натуральное число. Напишите программу, которая определяет,
# состоит ли указанное число из одинаковых цифр.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести «YES» если число состоит из одинаковых цифр и «NO» в противном случае.

num, flag, counter, last_num = int(input()), True, 0, 0
while num != 0:
    counter += 1
    last_digit = num % 10
    if counter == 1:
        last_num = last_digit
    if last_num != last_digit:
        flag = False
    num = num // 10
if flag:
    print('YES')
else:
    print('NO')
