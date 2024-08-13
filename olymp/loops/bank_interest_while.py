# Задача №3063. Банковские проценты
#
# # Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов, после чего дробная часть копеек
# отбрасывается. Каждый год сумма вклада становится больше. Определите, через сколько лет вклад составит не менее y
# рублей.
#
# Входные данные
# Программа получает на вход три натуральных числа: x, p, y.
#
# Выходные данные
# Программа должна вывести одно целое число.
#
# Примеры
# входные данные
# 100
# 10
# 200
# выходные данные
# 8

x = int(input("Enter first amount of money: "))
p = int(input("Enter the percent of changing: "))
y = int(input("Enter the final amount of money you need to reach: "))

n = 0

while x <= y:
    x = int(x * 1.1)
    n = n + 1

print(n)

