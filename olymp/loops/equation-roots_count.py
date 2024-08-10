# Задача №350. Количество решений
#
#
# Входные данные
# Вводятся 5 чисел: a, b, c, d и e.
#
# Выходные данные
# Найдите все целые решения уравнения (ax**3 + bx**2 + cx + d) / (x - e) = 0 на отрезке [0,1000] и
# выведите их количество.
#
# Примеры
# Входные данные
# 2
# 4
# 9
# 1
# 5
# Выходные данные
# 0


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
e = int(input("Enter fifth number: "))

res = 0

for x in range(0, 1000):
    if x - e != 0:
        if (a * x ** 3 + b * x ** 2 + c * x + d) / (x - e) == 0:
            res = res + 1
print(res)
