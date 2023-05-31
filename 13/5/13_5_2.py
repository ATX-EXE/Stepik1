# TODO Is Valid Triangle?
#
# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True если существует невырожденный
# треугольник со сторонами side1, side2, side3 и False в противном случае.
#
# Примечание 1. С данной задачей мы уже сталкивались при изучении условного оператора.

# объявление функции
def is_valid_triangle(side1, side2, side3):
    return side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))
