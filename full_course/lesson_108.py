# С помощью оператора = присвоить переменной user_name значение admin.
# Распечатать результат
user_name = 'admin'
print(user_name)

# С помощью оператора + сложить целые значения 10 и 20 и присвоить int_sum.
# Распечатать результат
int_sum = 10 + 20
print(int_sum)

# С помощью оператора + сложить два числа 10.1 и 19.9 и присвоить int_float.
# Распечатать результат
int_float = 10.1 + 19.9
print(int_float)

# С помощью оператора + сложить две строки Hello и World и присвоить int_str.
# Распечатать результат
int_str = 'Hello' + 'World'
print(int_str)

# С помощью оператора - вычесть из числа 20 число 10 и присвоить int_subtract.
# Распечатать результат
int_subtract = 20 - 10
print(int_subtract)

# С помощью оператора - вычесть из числа 20.2 число 10.1 и присвоить float_subtract.
# Распечатать результат
float_subtract = 20.2 - 10.1
print(float_subtract)

# С помощью оператора * перемножить два 20 и 10 и присвоить int_multiply.
# Распечатать результат
int_multiply = 20 * 10
print(int_multiply)

# С помощью оператора / разделить два 20 и 10 и присвоить int_divide.
# Распечатать результат
int_divide = 20 / 10
print(int_divide)

# Раздели число 50 пополам, и сохрани результат в int_divide_2.
# Распечатать результат и убедиться, что выводится 25.
int_divide_2 = 50 / 2
print(int_divide_2)

# С помощью оператора % посчитай остаток от деления 15 на 10 и запиши его в modulo_value.
# Распечатать результат и убедиться, что выводится 5.
modulo_value = 15 % 10
print(modulo_value)

# Напишите программу, которая запрашивает у пользователя целое число и выводит сообщение о том, является ли оно
# четным или нечетным.
num = int(input('Enter the number: '))
if num % 2 == 0:
    print('Number is even')
else:
    print('Number is odd')

# С помощью оператора // посчитай результат целочисленного деления 15 на 10 и запиши его в int_division.
# Распечатать результат и убедиться, что выводится 1.
int_division = 15 // 10
print(int_division)

# С помощью оператора // посчитай результат целочисленного деления 29 на 7 и запиши его в int_division_2.
# Распечатать результат и убедиться, что выводится 4.
int_division_2 = 29 // 7
print(int_division_2)

# С помощью оператора == сравнить два числа и записать значение в compare_ints.
# Распечатать compare_ints и убедиться, что он выводит True
a = 10
b = 10
compare_ints = a == b
print(compare_ints)

# С помощью оператора == сравнить две строки и записать значение в compare_strs.
# Распечатать compare_strs и убедиться, что он выводит True
str_1 = "Hello"
str_2 = "Hello"
compare_strs = str_1 == str_2
print(compare_strs)

# С помощью оператора == сравнить два числа и записать значение в compare_ints_2.
# Распечатать compare_ints_2 и убедиться, что он выводит False
a_2 = 20
b_2 = 10
compare_ints_2 = a_2 == b_2
print(compare_ints_2)

# С помощью оператора == сравнить две строки и записать значение в compare_strs_2.
# Распечатать compare_strs_2 и убедиться, что он выводит False
str_3 = "Hello"
str_4 = "hello"
compare_strs_2 = str_3 == str_4
print(compare_strs_2)

# С помощью оператора != сравнить два числа и записать значение в compare_ints_3.
# Распечатать compare_ints_3 и убедиться, что он выводит True
a_3 = 20
b_3 = 10
compare_ints_3 = a_3 != b_3
print(compare_ints_3)

# С помощью оператора > сравнить, что число a_4 больше числа b_4 и записать значение в compare_ints_4.
# Распечатать compare_ints_4 и убедиться, что он выводит True
a_4 = 20
b_4 = 10
compare_ints_4 = a_4 > b_4
print(compare_ints_4)

# С помощью оператора < сравнить, что число a_5 меньше числа b_5 и записать значение в compare_ints_5.
# Распечатать compare_ints_5 и убедиться, что он выводит False
a_5 = 20
b_5 = 10
compare_ints_5 = a_5 < b_5
print(compare_ints_5)

# С помощью оператора and вычислить, что число a_6 меньше числа b_6 и a7 больше b7 и записать значение в compare_ints_6.
# Распечатать compare_ints_6 и убедиться, что он выводит True
a_6 = 10
b_6 = 20
a_7 = 30
b_7 = 5
compare_ints_6 = a_6 < b_6 and a_7 > b_7
print(compare_ints_6)

# С помощью оператора or вычислить, что число a_8 меньше числа b_8 или a9 больше b9 и записать значение в compare_ints_8
# Распечатать compare_ints_8 и убедиться, что он выводит True
a_8 = 40
b_8 = 20
a_9 = 30
b_9 = 5
compare_ints_8 = a_8 < b_8 or a_9 > b_9
print(compare_ints_8)