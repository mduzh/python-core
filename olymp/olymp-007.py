# В файле data/olymp-007-in.txt строки.
# Нужно переставить местами 2 и 3 строку и вывести результат в файл tmp/olymp-007-out.txt

# Подсказка
# - Читаем по строкам содержимое файла в список строк (смотри решение в olymp-006.py)
# - Потом нужно в списке str_list поменять 2-й элемент с третьим
# - Потом открываем файл tmp/olymp-007-out.txt на запись
# - проходим циклом по всем элементам str_list и пишем их в выходной файл

str_list = []
file = open('../data/olymp-007-in.txt', 'r')
for s in file:
    str_list.append(s)
file.close()

ss = str_list[1]
str_list[1] = str_list[2]
str_list[2] = ss

out = open('../tmp/olymp-007-out.txt', 'w')
for s1 in str_list:
    out.write(s1)
out.close()