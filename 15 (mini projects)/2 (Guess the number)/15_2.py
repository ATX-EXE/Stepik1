# TODO Project - Угадайка чисел 🔃
# Описание проекта: программа генерирует случайное число
# в диапазоне от 1 до 100 и просит пользователя угадать это число.
# Если догадка пользователя больше случайного числа,
# то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'.
# Если догадка меньше случайного числа, то программа должна вывести сообщение
# 'Слишком мало, попробуйте еще раз'. Если пользователь угадывает число,
# то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.
#
# Составляющие проекта:
#
# Целые числа (тип int);
# Переменные;
# Ввод / вывод данных (функции input() и print());
# Условный оператор (if/elif/else);
# Цикл while;
# Бесконечный цикл;
# Операторы break, continue;
# Работа с модулем random для генерации случайных чисел.

# 1. Добавьте подсчет попыток, сделанных пользователем. Когда число отгадано,
# программа должна показать количество попыток;
# 2. Добавьте возможность генерации нового числа (повторная игра), после того,
# как пользователь угадал число;
# 3. Добавить возможность указания правой границы
# для случайного выбора числа (от 1 до n).

import random


def number_to_words(num):
    ones = ['ноль', 'один', 'два', 'три', 'четыре',
            'пять', 'шесть', 'семь', 'восемь', 'девять',
            'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
            'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['ноль', 'десять', 'двадцать', 'тридцать', 'сорок',
            'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if num < 20:
        return ones[num]
    else:
        if num % 10 == 0:
            return tens[num // 10]
        else:
            return tens[num // 10] + ' ' + ones[num % 10]


def is_valid(st):
    # return True if st.isdigit() else False
    if st.isdigit():
        print('TEST is_valid True')
        return True
    else:
        print('TEST is_valid False')
        return False


def borders_num(answer):
    while True:
        st = input()
        # return int(st) if is_valid(st) else print(answer)
        if is_valid(st):
            st = int(st)
            if st > 1 and st < 100000:
                print('TEST borders_num True')
                return st
        else:
            print('TEST borders_num False')
            print(answer)


def input_num(answer):
    while True:
        st = input()
        # return int(st) if is_valid(st) else print(answer)
        if is_valid(st):
            print('TEST input_num True')
            st = int(st)
            return st
        else:
            print('TEST input_num False')
            print(answer)


# игровой цикл
print('Добро пожаловать в числовую угадайку')
while True:
    print('Введите правую границу числа:')
    last_num = input_num('Требуется ввести число больше 1')
    num = random.randint(1, last_num)
    attempts = 0

    print('TEST Generated: ', num)
    print('Угадай число от 1 до', last_num)
    while True:
        player_num = input_num(('А может быть все-таки введем целое число от 1 до ', last_num, '?'))
        attempts += 1
        print('Попытка', number_to_words(attempts), '- Число', player_num)
        if player_num > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        if player_num < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        if player_num == num:
            print('Вы угадали, поздравляем!')
            break
    print('Играем еще раз? (y/n)')
    if input().lower() != 'y':
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
