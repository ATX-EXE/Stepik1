# TODO Удаление фрагмента
#
# На вход программе подается строка текста, в которой буква «h»
# встречается минимум два раза. Напишите программу, которая
# удаляет из этой строки первое и последнее вхождение буквы «h»,
# а также все символы, находящиеся между ними.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

s, word = input(), 'h'
num1, num2 = s.find(word), s.rfind(word) + 1
print(s[:num1] + s[num2:])
