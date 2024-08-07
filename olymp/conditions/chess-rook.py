# Задача №254. Ладья
#
# Требуется определить, бьет ли ладья, стоящая на клетке с указанными координатами (номер строки и номер столбца),
# фигуру, стоящую на другой указанной клетке.
#
# Входные данные
# Вводятся четыре числа: координаты ладьи (два числа) и координаты другой фигуры (два числа), каждое число вводится в
# отдельной строке. Координаты - целые числа в интервале от 1 до 8.
#
# Выходные данные
# Требуется вывести слово YES, если ладья сможет побить фигуру за 1 ход и NO - в противном случае.
#
# Примеры
# входные данные
# 1
# 1
# 2
# 2
# выходные данные
# NO
# входные данные
# 1
# 1
# 2
# 1
# выходные данные
# Yes

x_1 = int(input('Enter the column of the beaten figure: '))
y_1 = int(input('Enter the line of the beaten figure: '))
x_2 = int(input('Enter the column of the rook: '))
y_2 = int(input('Enter the line of the rook: '))

if x_1 == x_2 or y_1 == y_2:
    print('YES')
else:
    print('NO')