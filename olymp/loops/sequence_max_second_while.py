# Задача №3070. Второй максимум
#
# Внимание: В задаче нельзя использовать списки!
#
# Последовательность состоит из различных натуральных чисел и завершается числом 0. Определите значение второго по
# величине элемента в этой последовательности.
#
# Числа, следующие за числом 0, считывать не нужно.
#
# Входные данные
# Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит).
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# Входные данные
# 1
# 7
# 9
# 0
# Выходные данные
# 7
# Входные данные
# 2
# 1
# 0
# Выходные данные
# 1

total = 0
max_num = -1
second_max_num = -1
while True:
    num = int(input("Enter your number: "))
    if num == 0:
        break
    if num > max_num:
        second_max_num = max_num
        max_num = num
    elif second_max_num < num < max_num:
        second_max_num = num
print(second_max_num)

