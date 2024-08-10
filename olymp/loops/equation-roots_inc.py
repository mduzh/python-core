# Задача №348. Уравнение по возрастанию
#
#
# Входные данные
# Вводятся 4 числа: a, b, c и d.
#
# Выходные данные
# Найдите все целые решения уравнения ax**3 + bx**2 + cx + d = 0 на отрезке [0,1000] и выведите их в порядке
# возрастания. Если на данном отрезке нет ни одного решения, то ничего выводить не нужно.
#
# Примеры
# Входные данные
# 1
# -5
# 6
# 0
# Выходные данные
# 0 2 3

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

res = 0

for x in range(0, 1001):
    if a * (x**3) + b * (x**2) + c * x + d == 0:
        res = x
        print(res, end=" ")


