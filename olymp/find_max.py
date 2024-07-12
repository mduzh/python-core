# Напишите программу, которая запрашивает у пользователя список чисел, разделенных пробелами, и находит
# наибольшее число в этом списке.

# Подсказка: см. count_even_odd.py - там есть как разобрать строку.
values_str = input('Enter the list of numbers: ')

str_values_lst = values_str.split()

max_value = 0
for str_value in str_values_lst:
    int_value = int(str_value)
    if int_value > max_value:
        max_value = int_value

print(max_value)
