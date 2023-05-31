# TODO Обратное число
#
# Напишите программу, которая считывает с клавиатуры одно число
# и выводит обратное (https://ru.wikipedia.org/wiki/Обратное_число) ему.
# Если при этом введённое с клавиатуры число – ноль, то вывести
# «Обратного числа не существует» (без кавычек).
#
# Формат входных данных
# На вход программе подается одно действительное число.
#
# Формат выходных данных
# Программа должна вывести действительное число обратное данному,
# либо текст в соответствии с условием задачи.

num = float(input())
if num == 0:
    print('Обратного числа не существует')
else:
    # print(1 / num)
    print(num ** -1)
