# Задача №109. Две одинаковые буквы
#
# Дана строка. Известно, что она содержит ровно две одинаковые буквы. Найдите эти буквы. Гарантируется,
# что повторяются буквы только одного вида.
#
# Код должен содержать 2 решения:
# - используя функцию count у строк. Создаете цикл по всем символам строки s. И в теле цикла проверяете, сколько раз
# текущий символ входит в строку s через метод count. Если ответ 2, то печатаете символ и выходите. Иначе идете к
# следующему символу.
# - свое решение. Можно сделать так: создаете цикл по всем символам строки s. И в теле цикла делаете еще один цикл,
# который еще раз проходит по той же строке и считает, сколько раз символ из внешнего цикла встречается в строке.
# Если ответ 2, то выходите из внешнего цикла. Если нет, то считаете для следующего элемента во внешнем цикле.
#
#
# Входные данные
# На вход подается 1 строка.
#
# Выходные данные
# Необходимо вывести  букву, которая встречается в строке дважды.
#
# Примеры
# Входные данные
# fif
# Выходные данные
# f

string = input("Enter your string: ")

for s in string:
    if string.count(s) == 2:
        print(s)
        break


for s in string:
    counter = 0
    for el in string:
        if s == el:
            counter += 1
    if counter == 2:
        print(s)
        break
