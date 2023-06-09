# TODO Корни уравнения 🌶️🌶️
#
# Напишите функцию solve(a, b, c), которая принимает в качестве аргументов
# три целых числа a, b, c – коэффициенты квадратного уравнения
# ax^2+bx+c=0 и возвращает его корни в порядке возрастания.
#
# Примечание 1. С подобной задачей мы уже сталкивались.
#
# Примечание 2. Гарантируется, что квадратное уравнение имеет корни.

# объявление функции
def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    # if d < 0:
    #     print('Нет корней')
    # elif d == 0:
    #     print((-b / (2 * a)))
    # else:
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    if x1 < x2:
        return x1, x2
    else:
        return x2, x1


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
