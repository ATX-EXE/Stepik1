# TODO Возрастная группа
#
# Напишите программу, которая по введённому возрасту пользователя сообщает,
# к какой возрастной группе он относится:
#
# до 13 включительно – детство;
# от 14 до 24 – молодость;
# от 25 до 59 – зрелость;
# от 60 – старость.
# Формат входных данных
# На вход программе подаётся одно целое число – возраст пользователя.
#
# Формат выходных данных
# Программа должна вывести название возрастной группы.

num = int(input())
if num <= 13:
    print('детство')
if 13 < num < 25:
    print('молодость')
if 24 < num < 60:
    print('зрелость')
if 59 < num:
    print('старость')
