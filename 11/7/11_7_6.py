# TODO Список числовых полиндромов
#
# Дополните приведенный код, используя списочное выражение, так чтобы
# получить список всех чисел палиндромов от 100 до 1000.

palindromes = [i for i in range(100, 1000) if i // 100 == i % 10]
print(palindromes)
