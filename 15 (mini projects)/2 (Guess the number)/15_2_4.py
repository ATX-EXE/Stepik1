# TODO Тимур и его числа
#
# Тимур загадал число от 1 до n. За какое наименьшее количество вопросов
# (на которые Тимур отвечает "больше" или "меньше") Руслан может
# гарантированно угадать число Тимура?
#
# Формат входных данных
# На вход программе подается натуральное число n.
#
# Формат выходных данных
# Программа должна вывести наименьшее количество вопросов, которых
# гарантированно хватит Руслану, чтобы угадать число Тимура.

from math import log2, ceil

n = int(input())

print(int(ceil(log2(n))))
