# TODO Аве, Цезарь 🌶️
# На вход программе подаётся строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются строчными, а прописные – прописными. Гарантируется, что между различными словами присутствует один пробел.
#
# Формат входных данных
# На вход программе подаётся строка текста на английском языке.
#
# Формат выходных данных
# Программа должна вывести зашифрованный текст в соответствии с условием задачи.
#
# Примечание. Символы, не являющиеся английскими буквами, не изменяются.
from os.path import split


def alphabet_english_lower():
    return "".join([chr(char) for char in range(ord("a"), ord("z") + 1)])


def alphabet_english_upper():
    return "".join([chr(char) for char in range(ord("A"), ord("Z") + 1)])


def alphabet_russian_lower():
    return "".join([chr(char) for char in range(ord("а"), ord("я") + 1)])


def alphabet_russian_upper():
    return "".join([chr(char) for char in range(ord("А"), ord("Я") + 1)])


dictionary = []
dictionary.append(alphabet_english_lower())
dictionary.append(alphabet_english_upper())
dictionary.append(alphabet_russian_lower())
dictionary.append(alphabet_russian_upper())


def cript_letter(letter_, shift_):
    if letter_ in dictionary[0]:
        return dictionary[0][(dictionary[0].index(letter_) + shift_) % len(dictionary[0])]
    elif letter_ in dictionary[1]:
        return dictionary[1][(dictionary[1].index(letter_) + shift_) % len(dictionary[1])]
    elif letter_ in dictionary[2]:
        return dictionary[2][(dictionary[2].index(letter_) + shift_) % len(dictionary[2])]
    elif letter_ in dictionary[3]:
        return dictionary[3][(dictionary[3].index(letter_) + shift_) % len(dictionary[3])]
    else:
        return letter_


def cript_string(str_in_, shift_):
    str_out_ = ""
    for i in str_in_:
        str_out_ = str_out_ + str(cript_letter(i, shift_))
    return str_out_

def len_(word_):
        shift_ = 0
        for i in word_:
            if i.isalpha():
                shift_ += 1
        return shift_


# str_in, shift = input("String: "), input("Keys: ")
str_in, str_out = input().split(), []

for i in str_in:
    str_out.append(cript_string(i, len_(i)))

print(" ".join(str_out))
