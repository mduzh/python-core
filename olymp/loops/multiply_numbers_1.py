# Задача. Перемножение чисел

# По данному натуральному n перемножьте число k n раз, т.е. k * k * k * ... * k и так n раз
#
# Входные данные
# Вводится целые положительные числа n и к
#
# Выходные данные
# Необходимо вывести вычисленную сумму.
#
# Примеры
# Входные данные
# 3
# 3
# Выходные данные
# 27
#
# Входные данные#
# 3
# 2
# Выходные данные
# 8

n = int(input('Enter first number: '))
k = int(input('Enter second number: '))

res = 1
for value in range(1, n + 1):
    res = res * k
print(res)