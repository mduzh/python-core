# Задача. Сумма чисел

# По данному натуральному n сложите число k n раз, т.е. k + k + k + k и так n раз
#
# Входные данные
# Вводится целые положительные числа n и к
#
# Выходные данные
# Необходимо вывести вычисленную сумму.
#
# Примеры
# Входные данные
# 5
# 3
# Выходные данные
# 15
#
# Входные данные#
# 2
# 10
# Выходные данные
# 20

n = int(input('Enter first number: '))
k = int(input("Enter second number: "))
res = 0
for value in range(1, n + 1):
    res = res + k
print(res)