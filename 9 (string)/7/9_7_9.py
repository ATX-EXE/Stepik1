# TODO Самое тяжёлое слово 🗿
#
# Под "тяжестью" слова будем понимать сумму кодов по таблице Unicode
# всех символов этого слова. Напишите программу, которая принимает 4 слова
# и находит среди них самое тяжёлое слово. Если самых тяжёлых слов будет несколько,
# то программа должна вывести первое из них.

word, count = '', 0
for i in range(4):
    input_word = input()
    input_count = 0
    for j in input_word:
        input_count += ord(j)
    if input_count>count:
        word, count = input_word, input_count
print(word)
