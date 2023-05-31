# TODO Random - Функция shuffle()
# принимает список в качестве обязательного аргумента и
# перемешивает его случайным образом.

import random

print('\n' + 'Random - Функция shuffle()')
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)
print(numbers)

# TODO Random - Функция choice()
# принимает список (строку) в качестве обязательного аргумента и
# возвращает один случайный элемент из переданного списка (строки).

import random

print('\n' + 'Random - Функция choice()')
print(random.choice('BEEGEEK'))
print(random.choice([1, 2, 3, 4]))
print(random.choice(['a', 'b', 'c', 'd']))

# TODO Random - Функция sample()
# принимает два обязательных аргумента: список (строку) и
# количество случайных элементов, а возвращает список
# случайных элементов в указанном количестве.

import random

numbers = [2, 5, 8, 9, 12]

print('\n' + 'Random - Функция sample()')
print(random.sample(numbers, 1))
print(random.sample(numbers, 2))
print(random.sample(numbers, 3))
print(random.sample(numbers, 5))
