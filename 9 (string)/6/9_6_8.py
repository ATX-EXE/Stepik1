# TODO Используя f-строку, дополните приведённый ниже код так, чтобы он вывел текст:
#
# In 2010, someone paid 10K Bitcoin for two pizzas.
#
# s = 'In {}, someone paid {} {} for two pizzas.'
# print()

year, cost, foregan = 2010, '10K', 'Bitcoin'
s = f'In {year}, someone paid {cost} {foregan} for two pizzas.'
print(s)