# Задача №1479.
# В книге на одной странице помещается k строк. Таким образом, на 1-й странице печатаются строки с 1-й по k-ю,
# на второй — с (k+1)-й по (2k)-ю и т. д. Напишите программу, по номеру строки в тексте определяющую номер страницы,
# на которой будет напечатана эта строка, и порядковый номер этой строки на странице.
#
# Входные данные
# На вход программе подаются число k — количество строк на странице и
# число n — номер строки в тексте (1≤k≤200, 1≤n≤20000).
#
# Выходные данные
# Выведите два числа — номер страницы, на которой будет напечатана эта строка, и номер строки на этой странице
#
# Примечание: Для считывания данных нужно строку разбить несколько строк с разделителем пробел - мы такое вроде уже
# делали, поищите.
#
# k, n = map(int, input().split())
#
# Примеры
# Входные данные
# 50 1
# Выходные данные
# 1 1
# Входные данные
# 20 25
# Выходные данные
# 2 5
# Входные данные
# 15 43
# Выходные данные
# 3 13

# k = int(input("Enter the amount of ines on a page: "))
# n = int(input("Enter the number of a line in text: "))

value = input("Enter data: ")
values = value.split()

k = int(values[0])
n = int(values[1])

pages = n // k + 1
lines = n % k

print(pages, lines)