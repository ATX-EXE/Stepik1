# TODO Змеиный регистр
#
# Напишите функцию convert_to_python_case(text), которая принимает
# в качестве аргумента строку в «верблюжьем регистре» и преобразует
# его в «змеиный регистр».
#
# Примечание. Следующий программный код:
# print(convert_to_python_case('ThisIsCamelCased'))
# print(convert_to_python_case('IsPrimeNumber'))
# должен выводить:
# this_is_camel_cased
# is_prime_number

# объявление функции
def convert_to_python_case(text):
    total = ''
    for i in range(len(text)):
        if i == 0:
            total += text[0].lower()
            continue
        if text[i].isupper():
            total += '_' + text[i].lower()
        else:
            total += text[i]
    return total


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
