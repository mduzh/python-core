# В файле data/olymp-008-in.txt строки.
# Нужно вывести их файл в следующем порядке: поменять первую со второй, третью с четвертой, пятую с шестой.
# Т.е. нужно вывести
# a
# aa
# b
# bb
# и так далее. Количество строк в файле может быть любым четным числом
# Результат записать в файл tmp/olymp-008-out.txt

# Подсказка
# - Читаем по строкам содержимое файла в список строк (смотри решение в olymp-006.py)
# - Потом нужно в списке str_list поменять 0 с 1-м, 2-й с 3-м, и так далее
# - чтобы поменять, то делаем цикл с помощью while, где индекс меняется 0, 2, 4 и пр.
# - А для каждого индекса берем текущий элемент, следующи и меняем их
# - Потом открывае фай tmp/olymp-007-out.txt назапись
# - проходим циклом по всем элементам str_list и пишем их в выходной файл

in_file = open('../data/olymp-008-in.txt', 'r')
str_list = []
for s in in_file:
    str_list.append(s)
in_file.close()
print(str_list)

for index in range(0, len(str_list), 2):
    a = str_list[index]
    b = str_list[index + 1]
    str_list[index] = b
    str_list[index + 1] = a

print(str_list)

out_file = open('../tmp/olymp-008-out.txt', 'w')
for s in str_list:
    out_file.write(s)
out_file.close()