# Задача №106. Количество слов
#
# Дана строка, содержащая пробелы. Найдите, сколько в ней слов (слово – это последовательность непробельных символов,
# слова разделены одним пробелом, первый и последний символ строки – не пробел).
#
# Код должен содержать 2 решения:
# - используя встроенную функцию split для строки
# - свое решение (можно через цикл for пройти по всем символами и посчитать сколько пробелов. И из этого посчитать
# сколько слов. ну или свое что предложите)
#
#
# Входные данные
# На вход подается несколько строк.
#
# Выходные данные
# Необходимо вывести  количество слов в первой из введенных строк.
#
# Примеры
# входные данные
# In the town where I was born
# выходные данные
# 7

string = input("Enter your string: ")

string_list = string.split()
print(len(string_list))

total = 1
for s in string:
    if i == " ":
        total = total + 1
print(total)
