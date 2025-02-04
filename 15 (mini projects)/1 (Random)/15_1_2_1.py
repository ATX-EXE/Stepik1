# TODO кидаем 2 кубика

import random

again = 'y'
while again.lower() == 'y':
    print('Бросаем кубики... ')
    print('Значения граней:')
    print(random.randint(1, 6))
    print(random.randint(1, 6))
    again = input('Бросить кубики еще раз? (y = да, n = нет): ')