# Задача. Перемножение чисел

# По данному натуральному n перемножьте число (k + 2) n раз, т.е. (k+2) * (k+2) * ... * (k+2) и так n раз
#
# Входные данные
# Вводится целые положительные числа n и к
#
# Выходные данные
# Необходимо вывести вычисленную сумму.
#
# Примеры
# Входные данные
# 4
# 1
# Выходные данные
# 16 ! должно быть 81 !!!
#
# Входные данные#
# 3
# 2
# Выходные данные
# 125 ! должно быть 64 !!!

n = int(input('Enter first number: '))
k = int(input('Enter second number: '))

res = 1
for value in range(1, n + 1):
    res = res * (k + 2)
print(res)