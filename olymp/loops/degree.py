# Задача №352. Степень

# Напишите программу, вычисляющую 2 в степень N.
# Решить задачу 2-мя способами: с помощью цикла и с помощью **
#
# Входные данные
# Вводится целое неотрицательное число N, которое не превосходит 30.
#
# Выходные данные
# Выведите число 2 N.
#
# Примеры
# Входные данные
# 4
# Выходные данные
# 16

N = int(input('Enter the number: '))
print(2 ** N)

# res = 2 * 2 * 2 * 2 * 2
res = 1
for value in range(1, N + 1):
    res = res * 2
print(res)

res = 2
for value in range(2, N + 1):
    res = res * 2
print(res)