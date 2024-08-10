# Входные данные
# Вводятся 4 числа: a, b, c и d.
#
# Выходные данные
# Выведите все числа на отрезке от a до b, дающие остаток c при делении на d.
# Если таких чисел не существует, то ничего выводить не нужно.
#
# Примеры
# входные данные
# 2
# 5
# 0
# 2
# выходные данные
# 2 4

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

for value in range(a, b + 1):
    if value % d == c:
        print(value)