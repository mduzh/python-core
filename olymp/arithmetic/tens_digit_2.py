# Задача №2943. Число десятков
# Дано неотрицательное целое число. Найдите число десятков в его десятичной записи
# (то есть вторую справа цифру его десятичной записи).
#
# Входные данные
# Вводится неотрицательное целое число.
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# входные данные
# 179
# выходные данные
# 7

str_value = input('Enter your number: ')
res = str_value[-2]
print(res)