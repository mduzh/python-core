# Задача №2952. Разность времен
#
# Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, минуты и секунды для каждого из
# моментов времени. Известно, что второй момент времени наступил не раньше первого. Определите, сколько секунд прошло
# между двумя моментами времени.
#
# Входные данные
# Программа на вход получает три целых числа — часы, минуты, секунды, задающие первый момент времени и три целых числа,
# задающих второй момент времени.
#
# Выходные данные
# Выведите число секунд между этими моментами времени.
#
# Примеры
# входные данные
# 1
# 1
# 1
# 2
# 2
# 2
# выходные данные
# 3661
# входные данные
# 1
# 2
# 30
# 1
# 3
# 20
# выходные данные
# 50

hours_1 = int(input('Enter first hour: '))
minutes_1 = int(input('Enter first minutes: '))
seconds_1 = int(input('Enter first seconds: '))
hours_2 = int(input('Enter second hour: '))
minutes_2 = int(input('Enter second minutes: '))
seconds_2 = int(input('Enter second seconds: '))

hours_in_seconds_1 = hours_1 * 3600
minutes_in_seconds_1 = minutes_1 * 60

hours_in_seconds_2 = hours_2 * 3600
minutes_in_seconds_2 = minutes_2 * 60

total_second_1 = (hours_in_seconds_1 + minutes_in_seconds_1 + seconds_1)
total_second_2 = (hours_in_seconds_2 + minutes_in_seconds_2 + seconds_2)

res = total_second_2 - total_second_1
print(res)
