# Дано целое число n. Выведите следующее за ним нечетное число.
# При решении этой задачи нельзя использовать условную инструкцию if и циклы.
#
# Входные данные
# Вводится натуральное число.
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# входные данные
# 6
# выходные данные
# 7
# входные данные
# 3
# выходные данные
# 5

int_value = int(input('Enter your number: '))
if int_value % 2 != 0:
    int_value = int_value + 2
else:
    int_value = int_value + 1
print(int_value)