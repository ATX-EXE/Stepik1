# TODO Делители 2
#
# Напишите функцию number_of_factors(num), принимающую в качестве
# аргумента число и возвращающую количество делителей данного числа.
#
# Примечание 1. Используйте уже реализованную функцию get_factors(num)
# из предыдущей задачи.

# объявление функции
def get_factors(num):
    nums = list()
    for i in range(1, num + 1):
        if num % i == 0:
            nums.append(i)
    return len(nums)


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
