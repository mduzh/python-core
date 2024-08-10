# Задача №339. Минимальный делитель
#
#
# Найдите самый маленький натуральный делитель числа x, отличный от 1 (2 <= x <= 30000).
#
# Входные данные
# Вводится натуральное число x.
#
# Выходные данные
# Выведите наименьший делитель числа x, отличный от 1.
#
# Примеры
# Входные данные
# 6
# Выходные данные
# 2
#
# Входные данные
# 21
# Выходные данные
# 3
#
# Входные данные
# 77
# Выходные данные
# 7

x = int(input("Enter first number: "))

for i in range(2, x + 1):
    if x % i == 0:
        print(i)
        break

