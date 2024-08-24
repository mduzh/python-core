# Задача №1483.
#
# Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, потом минуты и секунды для каждого из
# моментов времени. Известно, что второй момент времени наступил не раньше первого. Определите, сколько секунд прошло
# между двумя моментами времени.
#
# Входные данные
# В первой строке входных данных находятся три целых числа — часы, минуты и секунды первого момента времени.
# Во второй строке — три числа, характеризующие второй момент времени.
# Число часов лежит в диапазоне от 0 до 23, число минут и секунд — от 0 до 59.
#
# Выходные данные
# Выведите число секунд между двумя моментами времени.
#
# Примеры
# Входные данные
# 1 1 1
# 2 2 2
# Выходные данные
# 3661
# Входные данные
# 1 2 30
# 1 3 20
# Выходные данные
# 50

value_1 = input("Enter first values of time: ")
value_2 = input("Enter second values of time: ")

values_1 = value_1.split()
values_2 = value_2.split()

h_1 = int(values_1[0])
m_1 = int(values_1[1])
s_1 = int(values_1[2])

h_2 = int(values_2[0])
m_2 = int(values_2[1])
s_2 = int(values_2[2])

res = ((h_2 * 3600) + (m_2 * 60) + s_2) - ((h_1 * 3600) + (m_1 * 60) + s_1)
print(res)