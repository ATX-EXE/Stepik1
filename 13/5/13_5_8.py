# TODO BEEGEEK
#
# BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.
#
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
# Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
#
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое
# значение пароля password и возвращает значение True если пароль является действительным паролем
# BEEGEEK банка и False в противном случае.
#
# Примечание. Следующий программный код:
# print(is_valid_password('1221:101:22'))
# print(is_valid_password('565:30:50'))
# print(is_valid_password('112:7:9'))
# print(is_valid_password('1221:101:22:22'))
#
# должен выводить:
# True
# False
# False
# False

# допоплнительные функции
# является ли палиндромом
def is_palindrome(num):
    for i in range(len(num) // 2):
        if num[i] != num[-(i + 1)]:
            return False
    return True


# является ли простым числом
def is_prime(num):
    return len([i for i in range(1, num + 1) if num % i == 0]) == 2


# является ли четным
def is_even(num):
    return num % 2 == 0


def is_valid_password(password):
    # Разбиваем на словарь с разделителем ":"
    p = password.split(":")
    # Если их 3 и в каждой только цифры - делаем проверки
    if len(p) != 3:
        return False
    # Проверка 1 (палиндром)
    # Проверка 2 (простое)
    # Проверка 3 (четное)
    if is_palindrome(p[0]) and is_prime(int(p[1])) and is_even(int(p[2])):
        return True
    else:
        return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
