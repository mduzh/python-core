# Задача №1466. Сумма от 1 до N
#
# Сумму всех целых чисел от 1 до 100 можно посчитать при помощи хитрого приема. Разобьем все числа по парам
# 1 и 100, 2 и 99, 3 и 98 и т.д. Сумма каждой пары 101. Пар всего 100 пополам (50).
# Поэтому сумма равна ((1+100)∗100)/2.
#
# Для нечетного количества слагаемых работает та же формула: например, 1+2+3=((1+3)*3)/2=6
#
# Входные данные
#
# Одно целое число N.
#
# N может быть отрицательным. Например, при N = -2, сумма будет 1 + 0 + -1 + -2 = -2.
#
# Выходные данные
# Одно число – сумма всех целых чисел от 1 до N.
#
# Примеры
# Входные данные
# 100
# Выходные данные
# 5050
# Входные данные
# 3
# Выходные данные
# 6

N = int(input("enter your number: "))

res = ((1 + N) * N) / 2
print(res)