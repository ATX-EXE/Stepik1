# TODO Алфавит
#
# Напишите программу, выводящую следующий список:
#
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
#
# Формат выходных данных
# Программа должна вывести указанный список.
# 
# Примечание. Последний элемент списка состоит из 26 символов z.

abc = 'abcdefghijklmnopqrstuvwxyz'
abc_list = list()
for i in abc:
    abc_str = ''
    for j in range(abc.find(i) + 1):
        abc_str += i
    abc_list.append(abc_str)
print(abc_list)
