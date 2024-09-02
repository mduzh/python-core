# Задача №1435. IP-адрес

# Для того чтобы выходить в Интернет, каждому компьютеру присваивается так называемый IP-адрес.
# Он состоит из четырех целых чисел в диапазоне от 0 до 255, разделенных точками.
# В следующих трех строках показаны три правильных IP-адреса:
#
# 127.0.0.0
# 192.168.0.01
# 255.00.255.255

# Напишите программу, которая определяет, является ли заданная строка правильным IP-адресом.

# Подсказка:
# Для определения того, является ли заданная строка правильным IP-адресом, нужно проверить следующие условия:
#
# 1. Строка должна состоять из четырех чисел, разделенных точками - можно строке сделать split на куски, разделенные
# точкой  и посмотреть, 4 ли их там.
# 2. Каждое число должно находиться в диапазоне от 0 до 255  - надо проверить, что каждый кусок строки является ли
# числом (используйте isdigit).
# 3. Числа не должны содержать ведущих нулей, за исключением самого числа "0" - проверить, если число 0
# (или substr[0] = "0"), то не должно быть длина substr больше ее, т.е 00 не может быть.


# Входные данные
# На вход программе подается строка длиной не более 15 символов, которая включает цифры и ровно три точки.
#
# Выходные данные
# Если строка является правильным IP-адресом, необходимо вывести 1, иначе 0.
#
# Примеры
# Входные данные
# 127.0.0.1
# Выходные данные
# 1
# Входные данные
# 12...34
# Выходные данные
# 0
# Входные данные
# 192.168.0.01
# Выходные данные
# 0
# Входные данные
# 255.00.255.255
# Выходные данные
# 0
