# Задача №303. Коровы

# По данному числу n закончите фразу "На лугу пасется..." одним из возможных продолжений: "n коров", "n корова",
# "n коровы", правильно склоняя слово "корова".
#
# Входные данные
# Дано число n (n<100).
#
# Выходные данные
# Программа должна вывести введенное число n и одно из слов (на латинице): korov, korova или korovy,
# например, 1 korova, 2 korovy, 5 korov. Между числом и словом должен стоять ровно один пробел.
#
# Примеры
# входные данные
# 1
# выходные данные
# 1 korova

n = int(input('Enter the amount of cows: '))

# if n == 1 or (n != 11 and n % 10 == 1):
#     print('На лугу пасется', n, 'корова')
# elif n in range(2, 5) or n % 10 in range(2, 5):
#     print('На лугу пасется', n, 'коровы')
# elif n in range(5, 21) or n % 10 in range(5, 10) or n == 11:
#     print('На лугу пасется', n, 'коров')

if n != 11 and n % 10 == 1:
    print('На лугу пасется', n, 'корова')
elif n % 10 in [2, 3, 4] and n not in [12, 13, 14]:
    print('На лугу пасется', n, 'коровы')
else:
    print('На лугу пасется', n, 'коров')


