# Задача №336. Цифра в числе
#
# Входные данные.
# Вводятся 2 числа: x и d.
#
# Выходные данные.
# Подсчитайте и выведите одно число - сколько раз встречается в записи натурального числа x цифра d.

x = input("Enter first number: ")
d = input("Enter second number: ")

res = 0
for value in x:
    if value == d:
        res = res + 1
print(res)