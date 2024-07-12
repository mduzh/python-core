# Дано натуральное число. Выведите его последнюю цифру.
#
# Входные данные
# Вводится натуральное число.
N = input('Enter your number: ')
int_list = []
for value in N:
    value_int = int(value)
    int_list.append(value_int)
print(int_list[-1])
# Выходные данные
# Выведите ответ на задачу.

# Примеры
# входные данные
# 179
# выходные данные
# 9

