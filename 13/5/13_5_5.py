# TODO Good password 🌶️
#
# Напишите функцию is_password_good(password), которая принимает в
# качестве аргумента строковое значение пароля password и возвращает
# значение True если пароль является надежным и False в противном случае.
#
# Пароль является надежным если:
#
# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.
#
# Примечание. Следующий программный код:
#
# print(is_password_good('aabbCC11OP'))
# print(is_password_good('abC1pu'))
# должен выводить:
#
# True
# False

# объявление функции
def is_password_good(password):
    is_strong: bool = False

    for i in range(10):
        if str(i) in password:
            is_strong = True
            break
    print(len(password))

    if not is_strong or \
            len(password) < 8 or \
            password == password.upper() or \
            password == password.lower():
        is_strong = False

    return is_strong


# считываем данные
txt: str = input()

# вызываем функцию
print(is_password_good(txt))
