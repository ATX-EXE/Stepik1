# TODO Цветовой микшер 🌶️
#
# Красный, синий и желтый называются основными цветами, потому что их
# нельзя получить путем смешения других цветов. При смешивании двух
# основных цветов получается вторичный цвет:
#
# если смешать красный и синий, то получится фиолетовый;
# если смешать красный и желтый, то получится оранжевый;
# если смешать синий и желтый, то получится зеленый.
# Напишите программу, которая считывает названия двух основных цветов
# для смешивания. Если пользователь вводит что-нибудь помимо названий
# «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке.
# В противном случае программа должна вывести название вторичного цвета,
# который получится в результате.
#
# Формат входных данных
# На вход программе подаются две строки, каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести полученный цвет смешения либо сообщение
# «ошибка цвета», если введён был не цвет.
#
# Примечание 1. Если смешать красный и красный, то получится красный и т.д.
#
# Примечание 2. Поиграйтесь с настоящим цветовым микшером 🙂
# (https://colorscheme.ru/color-names.html)

col_1, col_2 = input(), input()
if col_1 == col_2 == 'красный':
    print('красный')
elif col_1 == col_2 == 'желтый':
    print('желтый')
elif col_1 == col_2 == 'синий':
    print('синий')
elif (col_1 == 'красный' and col_2 == 'синий') or (col_1 == 'синий' and col_2 == 'красный'):
    print('фиолетовый')
elif (col_1 == 'красный' and col_2 == 'желтый') or (col_1 == 'желтый' and col_2 == 'красный'):
    print('оранжевый')
elif (col_1 == 'синий' and col_2 == 'желтый') or (col_1 == 'желтый' and col_2 == 'синий'):
    print('зеленый')
else:
    print('ошибка цвета')