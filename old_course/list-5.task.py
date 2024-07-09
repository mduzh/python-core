# Дан список положительных чисел. Найти максимальный элемент и вывести на экран
# Подсказка:
# - ввести переменную maximum и занести в нее 0 - там будет храниться максимальное число
# - идем for-ом не по элементам списка и проверяем: если элемент больше maximum, тогда в него заносим ткуещий элемент
# - когда цикл закончится, то в maximum будет максимально значение
maximum = 0
lst = [1, 3, 4, 7, 8, 10]
for number in lst:
    if number > maximum:
        maximum = number
print(maximum)

# Дан список положительных чисел. Найти минимальный элемент и вывести на экран
# Подсказка:
lst = [11, 3, 4, 7, 8, 10]
minimum = lst[0]
for number in lst:
    if number < minimum:
        minimum = number
print(minimum)

# Дан список положительных чисел. Найти максимальный и минимальный элемент и вывести на экран
# Подсказка:
# - нужно делать 2 проверки: одну проверять с максимумом, другую с минимумом
lst = [11, 3, 4, 7, 8, 10]
maximum = lst[0]
minimum = lst[0]
for number in lst:
    if number > maximum:
        maximum = number
for number in lst:
    if number < minimum:
        minimum = number
print(maximum, minimum)

maximum = lst[0]
minimum = lst[0]
for number in lst:
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number
print(maximum, minimum)

