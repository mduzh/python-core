# Задача №319. Геометрическая прогрессия
#
# По данному действительному числу a и натуральному n вычислите сумму 1+a+a**2+...+a**n,
# не используя формулу суммы геометрической прогрессии. Время работы программы должно быть пропорционально n.
#
# Входные данные
# Вводятся 2 числа - a и n.
#
# Выходные данные
# Необходимо вывести  значение суммы.
#
# Примеры
# входные данные
# 2
# 2
# выходные данные
# 7

a = int(input("Enter first number: "))
n = int(input("Enter second number: "))

res = 0
for i in range(0, n + 1):
    res = res + (a ** i)
print(res)