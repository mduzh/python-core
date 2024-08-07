# Задача №257. Конь
#
# Требуется определить, бьет ли конь, стоящий на клетке с указанными координатами (номер строки и номер столбца),
# фигуру, стоящую на другой указанной клетке.
#
# Входные данные
# Вводятся четыре числа: координаты коня и координаты другой фигуры. Все координаты - целые числа в интервале от 1 до 8.
#
# Выходные данные
# Программа должна вывести слово YES, если конь может побить фигуру за 1 ход, в противном случае вывести слово NO.
#
# Примеры
# входные данные
# 1
# 1
# 3
# 2
# выходные данные
# YES
# входные данные
# 1
# 1
# 3
# 3
# выходные данные
# NO

x_1 = int(input('Enter the column of the beaten figure: '))
y_1 = int(input('Enter the line of the beaten figure: '))
x_2 = int(input('Enter the column of the knight: '))
y_2 = int(input('Enter the line of the knight: '))

if abs(x_2 - x_1 == 2) and abs(y_2 - y_1 == 1) or abs(x_2 - x_1 == 1) and abs(y_2 - y_1 == 2):
    print('YES')
else:
    print('NO')
