# TODO Ровно в одном
#
# Напишите функцию is_one_away(word1, word2), которая принимает
# в качестве аргументов два слова word1 и word2 и возвращает значение True
# если слова имеют одинаковую длину и
# отличаются ровно в 1 символе и False в противном случае.

# объявление функции
def is_one_away(word1, word2):
    total: int = 0
    if len(word1) == len(word2):
        word1, word2 = list(word1), list(word2)
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                total += 1
    else:
        return False
    return True if total == 1 else False


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))
