# Задача №105. Совпадают ли строки?
#
# Напишите программу, определяющую, совпадают ли 2 строки.
#
# Код должен содержать 2 решения:
# - используя оператор ==
# - свое решение
#
# Входные данные
# Заданы 2 строки.
#
# Выходные данные
# Необходимо вывести слово yes, если строки совпадают, и слово no в противном случае.
#
# Примеры
# Входные данные
# a
# a
# Выходные данные
# yes

value_1 = input("Enter first value: ")
value_2 = input("Enter second value: ")

if value_1 == value_2:
    print("Yes")
else:
    print("No")

res = "No"
if len(value_1) == len(value_2):
    length = len(value_1)
    for i in range(0, length):
        if value_1[i] == value_2[i]:
            res = "Yes"
print(res)
