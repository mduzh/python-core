# Задача №347. Ноль или не ноль
#
# Проверьте, есть ли среди данных N чисел нули.
#
# Входные данные
# Вводится число N, а затем N чисел.
#
# Выходные данные
# Выведите YES, если среди введенных чисел есть хотя бы один нуль, или NO в противном случае.
#
# Примеры
# Входные данные
# 3
# 28
# 1
# 0
# Выходные данные
# YES
# Входные данные
# 1
# 28
# Выходные данные
# NO

N = int(input("Enter the amount of values: "))
num_list = []

for value in range(0, N):
    res = int(input("Enter your number: "))
    num_list.append(res)

for i in num_list:
    if i == 0:
        zero_here = "Yes"
    else:
        zero_here = "NO"
print(zero_here)