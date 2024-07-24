# Задача №262. Сдача
#
# Товар стоит a руб. b коп. За него заплатили c руб. d коп. Сколько сдачи требуется получить?
#
# Входные данные
# Вводятся 4 числа: a, b, c и d.
#
# Выходные данные
# Необходимо вывести 2 числа: e и f, число рублей и копеек, соответственно.
#
# Примеры
# входные данные
# 5
# 5
# 6
# 5
# выходные данные
# 1 0
# входные данные
# 2
# 17
# 2
# 18
# выходные данные
# 0 1

a = int(input('Enter first cost of amount of rub: '))
b = int(input('Enter first cost of amount of coin: '))
c = int(input('Enter second amount of rub: '))
d = int(input('Enter second amount of coin: '))

a_res = a * 100
c_res = c * 100

rem_res = (c_res + b) - (a_res + b)

rem_rub = rem_res // 100
rem_coin = rem_res % 100

print(rem_rub, ':', rem_coin)
