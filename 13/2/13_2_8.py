# TODO Звездный треугольник
#
# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
#
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;
# а затем выводит его.
#
# Примечание. Гарантируется, что основание треугольника – нечетное число.

def draw_triangle(fill, base):
    for i in range(1, base + 1):
        if i <= (base + 1) / 2:
            print(fill * i)
        else:
            print(fill * (base + 1 - i))


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
