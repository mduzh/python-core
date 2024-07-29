# Задача №266. Координатные четверти
#
# Даны координаты двух точек на плоскости, требуется определить, лежат ли они в одной координатной четверти или нет
# (все координаты отличны от нуля).
#
# Входные данные.
# Вводятся 4 числа: координаты первой точки (x1, y1) и координаты второй точки (x2, y2).
#
# Выходные данные
# Программа должна вывести слово YES, если точки находятся в одной координатной четверти, в противном случае вывести
# слово NO.
#
# Примеры
# входные данные
# 3
# 3
# 5
# 1
# выходные данные
# YES

x_1 = int(input('Enter first coordinate x: '))
y_1 = int(input('Enter first coordinate y: '))
x_2 = int(input('Enter second coordinate x: '))
y_2 = int(input('Enter second coordinate y: '))

if x_1 > 0 and y_1 > 0 and x_2 > 0 and y_2 > 0:
    print('YES')
elif x_1 < 0 and y_1 > 0 and x_2 < 0 and y_2 > 0:
    print('YES')
elif x_1 < 0 and y_1 < 0 and x_2 < 0 and y_2 < 0:
    print('Yes')
elif x_1 > 0 and y_1 < 0 and x_2 > 0 and y_2 < 0:
    print('Yes')
else:
    print('NO')
