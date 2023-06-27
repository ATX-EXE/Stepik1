# TODO Next Prime 🌶️🌶️
#
# Напишите функцию get_next_prime(num), которая принимает в качестве
# аргумента натуральное число num и возвращает первое простое
# число большее числа num.
#
# Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

# объявление функции
def is_prime(num):
    return len([i for i in range(1, num + 1) if num % i == 0]) == 2


# объявление функции
def get_next_prime(num):
    f = num + 1
    while not is_prime(f):
        f += 1
    return f


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
