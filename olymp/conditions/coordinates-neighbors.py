# Задача №1445. Координаты соседей

# Для клетки с координатами (x, y) в таблице размером M × N выведите координаты ее соседей.
# Соседними называются клетки, имеющие общую сторону.
#
# Входные данные
# Даны натуральные числа M, N, x, y (1 ≤ x ≤ M ≤ 109, 1 ≤ y ≤ N ≤ 109).
#
# Выходные данные
# В выходной файл выведите пары координат соседей этой клетки в произвольном порядке.
#
# Примеры
# входные данные
# 3 3
# 2 2
# выходные данные
# 2 1
# 1 2
# 2 3
# 3 2

M = int(input('Enter the length of the board: '))
N = int(input('Enter the width of the board: '))
x = int(input('Enter the x coordinate: '))
y = int(input('Enter the y coordinate: '))

if x + 1 <= M:
    print(x + 1, y)
if y + 1 <= N:
    print(x, y + 1)
if x - 1 >= 1:
    print(x - 1, y)
if y - 1 >= 1:
    print(x, y - 1)
