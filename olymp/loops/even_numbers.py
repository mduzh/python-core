# Задача №333. Четные числа
#
# Входные данные.
# Вводятся целые числа a и b. Гарантируется, что a не превосходит b
#
# Выходные данные
# Выведите (через пробел) все четные числа от a до b (включительно).
#
# Примеры
# входные данные
# 2
# 5
# выходные данные
# 2 4

a = int(input("Enter first number: "))
b = int(input("Enter second  number: "))

for value in range(a, b + 1):
    if value % 2 == 0:
        print(value)
