# Для заданного списка распечатать каждый элемент.
user_list = ['admin', 'guest', 'mike']
for i in user_list:
    print(i)

# Напиши программу, которая для списка чисел num_list и вычисляет их сумму.
# Подсказка: сначала нужно завести переменную sum_nums и запиши в нее 0, в которую будет добавляться число из списка.
# Распечатай результат sum_nums и убедись, что программа вывела 15.
num_list = [1, 2, 3, 4, 5]
sum_nums = 0
for i in num_list:
    sum_nums = sum_nums + i

print(sum_nums)

# Напиши программу, которая для списка чисел num_list_2 и вычисляет их произведение.
# Распечатай результат и убедись, что программа вывела 24.
num_list_2 = [1, 2, 3, 4]
total_price_2 = 1
for d in num_list_2:
    total_price_2 = total_price_2 * d

print(total_price_2)

# Напиши программу, которая находит и выводит минимальный элемент в списке чисел.
# Подсказка: сначала нужно завести переменную min_value, в которой будешь хранить минимальное значение.
# Для начала запиши в нее первый элемент из num_list_3.
# Потом будешь идти по списку с помощью цикла и сравнивать min_value с текущим элементом.
# Если он больше, занесешь в переменную min_value. В итоге в конце списка в min_value будет минимальное значение.
# Распечатай результат и убедись, что программа вывела 5.
print('1' * 10)
num_list_3 = [10, 21, 5, 40, 15]
min_value = num_list_3[0]
for m in num_list_3:
    if m < min_value:
        min_value = m

print(min_value)

# Напиши программу, которая находит и выводит максимальный элемент в списке чисел.
# Распечатай результат и убедись, что программа вывела 20.
print('1' * 10)
num_list_4 = [11, 20, 5, 16]
max_num = num_list_4[0]
for x in num_list_4:
    if x > max_num:
        max_num = x

print(max_num)
# Напиши программу, которая находит и выводит максимальный и минимальный элементы в списке чисел.
# Распечатай результат и убедись, что программа должна вывести 40 и 5.
num_list_5 = [10, 20, 5, 40, 15]
max_num = num_list_5[0]
min_num = num_list_5[0]
for int_5 in num_list_5:
    if int_5 > max_num:
        max_num = int_5

    if int_5 < min_num:
        min_num = int_5

print(max_num, ' ; ', min_num)

# Напиши программу, которая вычисляет среднее значение элементов списка чисел.
# Нужно сложить все элементы списка, а потом поделить на кол-во элементов списка (len используй)
# Распечатай результат и убедись,  программа должна вывести 3.
num_list_6 = [1, 2, 3, 4, 5]
total_num = 0
for int_sum in num_list_6:
    total_num = total_num + int_sum

result = total_num / len(num_list_6)
print(result)

# Для заданного списка распечатать каждый элемент используя range и доступ по индексу.
# Подсказка: Нужно сделать последовательность range для len(user_list_2), в ней будут
# числа: 0, 1, ..., len(user_list_2) -1. И тогда ты идешь по индексам и вытаскиваешь элементы из user_list_2
user_list_2 = ['john', 'andy', 'jane']
for i in range(len(user_list_2)):
    print(user_list_2[i])

# Для заданного списка price_list умножить каждый элемент на 2.
# Подсказка: нужно идти по индексам (range), обращаться к элементу по индексу и присваивать ему
# текущее значение умноженное на 2.
# Потом распечатать весь список price_list через print
# Потом распечатать в цикле каждый элемент списка price_list
price_list = [10, 20, 30]
for i in range(len(price_list)):
    price_list[i] = price_list[i] * 2
print(price_list)

for price in price_list:
    print(price)

# Для заданного списка age_list каждое число меньше 18 заменить на 0.
# Подсказка: нужно проверить текущее значение через if. Если условие выполняется, то элемент меняем на 0.
# Потом распечатать весь список age_list через print
age_list = [21, 10, 7, 30]
for i in range(len(age_list)):
    if age_list[i] < 18:
        age_list[i] = 0

print(age_list)

# Для заданного списка price_list_2 сложить только цены, которые идут под четными индексами, т.е. 0, 2, 4  и т.д.
# Результат вывести на экран. Должно быть 160.
# Есть несколько решений. Ниже постановка для каждого из них.

# Решение 1: Пройти по всем индексам списка и проверять, является ли индекс четным. И только тогда его в сумму добавить.
price_list_1 = [10, 20, 30, 40, 50, 50, 70, 80]
total_ind_price_1 = 0
for ind_even in range(len(price_list_1)):
    if ind_even % 2 == 0:
        total_ind_price_1 = total_ind_price_1 + price_list_1[ind_even]

print(total_ind_price_1)
# Решение 2: Сделать индекс с шагом 2 через range и значения по этим индексам добавлять в сумму. Это лучшее решение,
# так как цикл повторяется только 4 раза и нет проверок (if) - будет работать быстрее в 2 раза минимум.
price_list_2 = [10, 20, 30, 40, 50, 50, 70, 80]
total_price_2 = 0
for i in range(0, len(price_list_2), 2):
    total_price_2 = total_price_2 + price_list_2[i]

print(total_price_2)

# Для заданного списка price_list_3 сложить только цены, которые идут под нечетными индексами, т.е. 1, 3, и т.д.
# Результат вывести на экран. Должно быть 190.
# Подсказка: Сделать индекс через range с указанным начальным значением и шагом

price_list_3 = [10, 20, 30, 40, 50, 50, 70, 80]

total_price_3 = 0
for odd_index in range(1, len(price_list_3), 2):
    total_price_3 = total_price_3 + price_list_3[odd_index]

print(total_price_3)

# Для списка price_list_4 значения под четными индексами умножить на 10, а под нечетными на 100.
# Распечатать price_list_4 через принт. Результат должен быть [100, 100, 200, 200, 300, 300, 500, 500].
# Есть несколько решений. Ниже постановка для каждого из них.

# Решение 1: Пройти по всем индексам списка и проверять, является ли индекс четным. Если да, тогда взять элемент по
# индексу и умножить на 10 и сохранить в списке. Если нет, то умножить на 100 и сохранить в списке.
price_list_4 = [10, 1, 20, 2, 30, 3, 50, 5]
for i in range(len(price_list_4)):
    if i % 2 == 0:
        price_list_4[i] = price_list_4[i] * 10
    if i % 2 != 0:
        price_list_4[i] = price_list_4[i] * 100

print(price_list_4)

# Решение 2: Сделать индекс i от 0 с шагом 2 через range.
# Взять элемент по индексу i и умножить на 10.
# Взять элемент по индексу i + 1 и умножить на 100.
price_list_4 = [10, 1, 20, 2, 30, 3, 50, 5]
for ind_4 in range(0, len(price_list_4), 2):
    price_list_4[ind_4] = price_list_4[ind_4] * 10
    price_list_4[ind_4 + 1] = price_list_4[ind_4 + 1] * 100

print(price_list_4)

# Для списка price_list_5 нужно поменять местами четные и нечетные элементы, т.е 0 с 1, 2 с 3-м, и т.д.
# Распечатать price_list_5 через принт. Результат должен быть [1, 10, 2, 20, 3, 30, 5, 50].
# Подсказка: Будем идти по четным индексам, т.е. сделать индекс i от 0 с шагом 2 через range.
# А потом элемент под индексом i поменять местами с элементом с индексом i+1.
price_list_5 = [10, 1, 20, 2, 30, 3, 50, 5]

for i in range(0, len(price_list_5), 2):
    value = price_list_5[i]
    price_list_5[i] = price_list_5[i + 1]
    price_list_5[i + 1] = value

print(price_list_5)

print('-' * 10)
# Дан список price_list_6
price_list_6 = [10, 1, 20, 2, 30, 3, 50, 5]

# Задача 1: Вывести на экран все элементы price_list_6, которые идут после 2-го.
# Результат должен содержать числа: 20, 2, 30, 3, 50, 5
for i in range(2, len(price_list_6)):
    print(price_list_6[i])

# Задача 2: Создать список price_list_6_res и в него сложить  все элементы, которые идут после 2-го в price_list_6.
# Распечатать price_list_6_res. Результат должен быть [20, 2, 30, 3, 50, 5]
price_list_6_res = []

for i in range(2, len(price_list_6)):
    price_list_6_res.append(price_list_6[i])

print(price_list_6_res)

# Задача 3: Сложить все price_list_6, которые идут после 2-го.
# Распечатать результат. Результат должен содержать числа: 88
value_6 = 0
for sum_6 in range(2, len(price_list_6)):
    value_6 = value_6 + price_list_6[sum_6]

print(value_6)

# Задача 4: Для списка price_list_6 найти минимальный и максимальный элемент среди тех , которые идут после 2-го.
# Распечатать результат. Результат должен содержать числа: 3 и 50
max6 = price_list_6[2]
min6 = price_list_6[2]
for el in range(2, len(price_list_6)):
    if price_list_6[el] > max6:
        max6 = price_list_6[el]
    if price_list_6[el] < min6:
        min6 = price_list_6[el]

print(max6, min6)

#  Даны 2 списка, которые содержат все буквы, которы встречаются в некотором тексте и количество раз, сколько каждая
#  буква есть в это тексте.
# - letters - это список всех букв.
# - counts - это сколько каждая буква встречается в тексте.
letters = ['a', 'b', 'c', 'd', 'e']
counts = [10, 5, 5, 6, 11]
# Н-р, counts[0] (т.е. 10) - это сколько буква letters[0] (т.е. 'a') встречается в тексте.
# Н-р, counts[2] (т.е. 5) - это сколько буква letters[2] (т.е. 'b') встречается в тексте.
#
# Задача: для заданной буквы test_letter вывести, сколько раз она встречается в тексте.
#
# Подсказка: Чтобы найти информацию о букве двух массивах нужно знать индекс этой буквы в letters. А потом уже по этому
# индексу взять кол-во из counts. Поэтому алгоритм такой:
# - заводим переменную letter_ind и присваиваем ей начальное значение. Так как test_letter может и не быть в тексте и,
# соответственно в letters, так что нужно инициализировать любым значением меньше 0, скажем -1.
# - потом идем в цикле по letters. Если  буква равна test_letter, то сохраняем индекс в letter_ind.
# - после завершения цикла в letter_ind будет храниться индекс буквы test_letter или -1.
# - если letter_ind равно -1, тогда выводим на экран "Буква не найдена", иначе выводим количество раз этой буквы из
# counts по индексу letter_ind

letters = ['a', 'b', 'c', 'd', 'e']
counts = [10, 5, 5, 6, 11]

test_letter = 'd'

letter_ind = -1
for i in range(len(letters)):
    if letters[i] == test_letter:
        letter_ind = i

if letter_ind == -1:
    print('Буква не найдена')
else:
    print(counts[letter_ind])
