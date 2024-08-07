# Задача №298. Ход короля
#
# Поле шахматной доски определяется парой чисел (a, b), каждое от 1 до 8, первое число задает номер столбца,
# второе – номер строки. Заданы две клетки. Определите, может ли шахматный король попасть с первой клетки на вторую
# за один ход.
#
# Входные данные
# Даны 4 целых числа от 1 до 8 каждое, первые два задают начальную клетку, вторые два задают конечную клетку.
# Начальная и конечная клетки не совпадают. Числа записаны в отдельных строках.
#
# Выходные данные
# Программа должна вывести YES, если из первой клетки ходом короля можно попасть во вторую, или NO в противном случае.
#
# Примеры
# входные данные
# 4
# 4
# 5
# 5
# выходные данные
# YES

x_1 = int(input('Enter the first column: '))
y_1 = int(input('Enter the first line: '))
x_2 = int(input('Enter the second column: '))
y_2 = int(input('Enter the second line: '))
if abs(x_2 - x_1) <= 1 and abs(y_2 - y_1) <= 1:
    print('YES')
else:
    print('NO')
