# Задача №335. Квадраты
#
#
# Входные данные
# Вводятся целые числа a и b. Гарантируется, что a не превосходит b.
#
# Выходные данные
# Выведите все числа на отрезке от a до b, являющиеся полными квадратами, т.е. число, являющееся квадратом некоторого
# целого числа.
# Если таких чисел нет, то ничего выводить не нужно.
#
# Примеры
# входные данные
# 2
# 8
# выходные данные
# 4
import math

import datetime

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

start = datetime.datetime.now()
for value in range(a, b + 1):
    if value ** 2 in range(a, b + 1):
        print(value ** 2)
finish = datetime.datetime.now()
print(finish - start)

start = datetime.datetime.now()
for i in range(a, b + 1):
    x = math.sqrt(i)
    k = int(x)
    if k ** 2 == i:
        print(i)
finish = datetime.datetime.now()
print(finish - start)