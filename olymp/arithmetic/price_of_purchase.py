# Задача №2951. Стоимость покупки
#
# Пирожок в столовой стоит a рублей и b копеек. Определите, сколько рублей и копеек нужно заплатить за n пирожков.
#
# Входные данные
# Программа получает на вход три числа: a, b, n.
#
# Выходные данные
# Программа должна вывести два числа: стоимость покупки в рублях и копейках.
#
# Примеры
# входные данные
# 10
# 15
# 2
# выходные данные
# 20 30
# входные данные
# 2
# 50
# 4
# выходные данные
# 10 0

a = int(input('Enter the amount of byn: '))
b = int(input('Enter the amount of cent: '))
n = int(input('Enter the amount of bunnies: '))

total_byn = a * n
total_cent = b * n

rub_in_cent = total_cent // 100
rem_cents = total_cent % 100

total_byn = total_byn + rub_in_cent

print(total_byn, rem_cents)


