# import random
# from random import *

# TODO Random - Функция randint()
# принимает два обязательных аргумента a и b и возвращает
# случайное целое число из отрезка [a;b]

import random

print('\n' + 'Функция randint()')
for _ in range(10):
    for _ in range(10):
        print(random.randint(0, 99), end='\t')
    print()

# TODO Random - Функция randrange()
# принимает такие же аргументы, что и функция range()
# возвращает случайно выбранное число из последовательности чисел

# TODO Random - Функция random()
# возвращает случайное число с плавающей точкой (вещественное число)
# в диапазоне от 0.0 до 1.0 (исключая 1.0)

import random

print('\n' + 'Функция random()')
for _ in range(5):
    for _ in range(5):
        print(random.random(), end='\t')
    print()

# TODO Random - Функция uniform()
# тоже возвращает случайное число с плавающей точкой,
# но при этом она позволяет задавать диапазон для отбора значений

import random

print('\n' + 'Функция uniform()')

for _ in range(5):
    for _ in range(5):
        print(random.uniform(1.5, 98.4), end='\t')
    print()

# TODO Random - Функция seed()
# явно устанавливаем начальное значение для генератора случайных чисел

import random

print('\n' + 'Функция seed()')
random.seed(43)
for _ in range(5):
    for _ in range(5):
        print(random.randint(0, 99), end='\t')
