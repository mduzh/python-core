# Задача №104. Изменить регистр символа
#
# Измените регистр символа, если он был латинской буквой: сделайте его заглавным, если он был строчной буквой и
# наоборот.
#
# Код должен содержать 2 решения:
# - используя встроенную функцию upper для строки
# - свое решение
#
# Входные данные
# Задан единственный символ C.
#
# Выходные данные
# Необходимо вывести  получившийся символ.
#
# Примеры
# Входные данные
# q
# Выходные данные
# Q
# Входные данные
# W
# Выходные данные
# w

value = input("Enter your value: ")
print(value.swapcase())

lowers = "abcdefghijklmnopqrstuvwxyz"
uppers = "ABSDEFGHIJKLMNOPQRSTUVWXYZ"

ind_lower = -1
for i in range(0, len(lowers)):
    if lowers[i] == value:
        ind_lower = i
        break

if ind_lower != -1:
    print(uppers[ind_lower])
else:
    ind_upper = -1
    for i in range(0, len(uppers)):
        if uppers[i] == value:
            ind_upper = i
            break
    if ind_upper != -1:
        print(lowers[ind_upper])
