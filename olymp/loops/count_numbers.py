# Задача №346. Подсчет чисел
#
# Подсчитайте, сколько среди данных N чисел нулей, положительных чисел, отрицательных чисел.
#
# Входные данные
# Вводится число N, а затем N целых чисел.
#
# Выходные данные
# Необходимо вывести сначала число нулей, затем число положительных и отрицательных чисел.
#
# Примеры
# Входные данные
# 5
# 28
# 0
# 0
# 0
# 0
# Выходные данные
# 4 1 0
# Входные данные
# 10
# 1
# -1
# 0
# 2
# -3
# -4
# 0
# 0
# 0
# 0
# Выходные данные
# 5 2 3


N = int(input("Enter the amount of numbers: "))
num_list = []
total_zero = 0
total_positive = 0
total_negative = 0

for value in range(0, N):
    res = int(input("Enter your number: "))
    num_list.append(res)

for i in num_list:
    if i == 0:
        total_zero = total_zero + 1
    elif i % 2 == 0:
        total_positive = total_positive + 1
    else:
        total_negative = total_negative + 1
print(total_zero, total_positive, total_negative)
