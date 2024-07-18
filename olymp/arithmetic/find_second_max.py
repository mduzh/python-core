# Напишите программу, которая запрашивает у пользователя список чисел, разделенных пробелами, и находит второе
# наибольшее число в этом списке.
#
# Убедитесь, что для ввода: 10 20 4 45 99 результатом будет 45.

str_value = input('Enter the list of numbers: ')
str_value_list = str_value.split()

max_value = int(str_value_list[0])
for value in str_value_list:
    int_value = int(value)
    if int_value > max_value:
        max_value = int_value
print(max_value)

second_max_value = None
for value in str_value_list:
    int_value = int(value)
    if int_value != max_value:
        if second_max_value is None or int_value > second_max_value:
            second_max_value = int_value
print(second_max_value)
