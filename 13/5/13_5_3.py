# TODO Is a Number Prime? 🌶️
#
# Напишите функцию is_prime(num), которая принимает в качестве
# аргумента натуральное число и возвращает значение True если
# число является простым и False в противном случае.

# объявление функции
def is_prime(num):
    return len([i for i in range(1, num + 1) if num % i == 0]) == 2


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
