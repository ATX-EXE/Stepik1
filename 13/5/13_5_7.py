# TODO Палиндром 🌶️
#
# Напишите функцию is_palindrome(text), которая принимает
# в качестве аргумента строку text и возвращает значение True
# если указанный текст является палиндромом и False в противном случае.
#
# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях
#
# Примечание 2. При проверке считайте большие и маленькие
# буквы одинаковыми, а также игнорируйте пробелы, а также символы , . ! ? -.
#
# Примечание 3. Следующий программный код:
#
# print(is_palindrome('А роза упала на лапу Азора.'))
# print(is_palindrome('Gabler Ruby - burrel bag!'))
# print(is_palindrome('BEEGEEK'))
# должен выводить:
#
# True
# True
# False

# объявление функции
def is_palindrome(text):
    text_arr = []
    text = ''
    for l in text.lower():      # Сделать все буквы маленькими
        if l.isalpha():         # Удалить все знаки кроме букв
            text = text.__add__(l)
    text_arr = list(text)
    # Сравниваем
    for i in range(len(text_arr) // 2):
        if text_arr[i] != text_arr[-(i + 1)]:
            return False
    return True

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
