# Напишите программу, которая запрашивает у пользователя список чисел, разделенных пробелами, и вычисляет их
# среднее арифметическое.
# Убедиться, что 1 2 3 4 5 среднее арифметическое: 3.0
values_str = input("Enter the list of numbers: ")

values_str_list = values_str.split()

total_values_sum = 0
for val_sum in values_str_list:
    value_sum = int(val_sum)
    total_values_sum = total_values_sum + value_sum
res = total_values_sum / len(values_str_list)
print(res)
