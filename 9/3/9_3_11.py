# TODO Нижний регистр
#
# На вход программе подается строка. Напишите программу,
# которая подсчитывает количество буквенных символов
# в нижнем регистре.
#
# Формат входных данных
# На вход программе подается строка.
#
# Формат выходных данных
# Программа должна вывести количество буквенных
# символов в нижнем регистре.

s = input()
counter = 0
for i in range(len(s)):
    if s[i] in 'abcdefghijklmnopqrstuvwxyz':
        counter += 1
print(counter)
