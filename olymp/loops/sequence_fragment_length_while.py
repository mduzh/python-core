# Задача №3078. Максимальная длина монотонного фрагмента
#
# Дана последовательность натуральных чисел, завершающаяся число 0. Определите наибольшую длину монотонного фрагмента
# последовательности (то есть такого фрагмента, где все элементы либо больше предыдущего, либо меньше).
#
# Числа, следующие за числом 0, считывать не нужно.
# Входные данные
# Дана последовательность натуральных чисел, завершающаяся число 0.
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# входные данные
# 1
# 7
# 7
# 9
# 1
# 0
# выходные данные
# 2

max_count = 0
min_count = 0
prev_num = -1
count = 0
while True:
    num = int(input("Enter your number: "))
    if num == 0:
        break

    if num > prev_num:
        max_count += 1
    if num < min_count:
        min_count += 1

    prev_num = num