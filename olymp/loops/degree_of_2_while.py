# Задача №3060. Точная степень двойки
#
#
# Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки,
# или слово NO в противном случае.
#
# Использовать цикл while
# Операцией возведения в степень пользоваться нельзя!
#
# Входные данные
# Вводится натуральное число.
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# входные данные
# 1
# выходные данные
# YES
# входные данные
# 4
# выходные данные
# YES
# входные данные
# 5
# выходные данные
# NO

n = int(input("Enter your number: "))

res = "No"

i = 0
while 2 ** i <= n:
    if n == 2**i:
        res = "YES"
        break
    else:
        i = i + 1
print(res)


# for i in range(5):
#     print(i, end="")
#
# print("")
#
# i = 0
# while i < 5:
#     print(i, end="")
#     i = i + 1
# print("")
#
# i = 0
# while True:
#     if i >= 5:
#         break
#     print(i, end="")
#     i = i + 1
# print("")
#
#
# while True:
#     s = input("Enter: ")
#     if s == 'exit()':
#         print("Process finished with exit code 0")
#         break
#     else:
#         print("You entered:", s)
