# Напишите программу, которая запрашивает у пользователя список чисел, разделенных пробелами, и подсчитывает количество
# положительных и отрицательных чисел в этом списке.
# Убедитесь, что для ввода: -1 2 -3 4 -5 будет распечатан результат 2 и 3
values_str = input("Enter the list of numbers: ")

values_str_list = values_str.split()

positive_list = []
negative_list = []
for value in values_str_list:
    int_value = int(value)
    if int_value > 0:
        positive_list.append(int_value)
    if int_value < 0:
        negative_list.append(int_value)

print(len(positive_list))
print(len(negative_list))