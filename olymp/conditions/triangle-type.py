# Задача №302. Тип треугольника

# Определите тип треугольника (остроугольный, тупоугольный, прямоугольный) с данными сторонами.
#
# Входные данные
# Даны три натуральных числа – стороны треугольника.

# Выходные данные
# Необходимо вывести одно из слов:
# - right для прямоугольного треугольника,
# - acute для остроугольного треугольника,
# - obtuse для тупоугольного треугольника или
# - impossible, если входные числа не образуют треугольника.
#
# Примеры
# входные данные
# 3
# 4
# 5
#
# выходные данные
# right

a = int(input('Enter first side: '))
b = int(input('Enter second side: '))
c = int(input('Enter third side: '))

if (a * a + b * b == c * c) or (a * a + c * c == b * b) or (c * c + b * b == a * a):
    print('right')
elif (a * a + b * b > c * c) or (a * a + c * c > b * b) or (c * c + b * b > a * a):
    print('acute')
elif (a * a + b * b < c * c) or (a * a + c * c < b * b) or (c * c + b * b < a * a):
    print('obtuse')
else:
    print('Impossible')