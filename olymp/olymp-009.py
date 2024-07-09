# В файле data/olymp-009-in.txt строки.
# Нужно вывести их файл в следующем порядке: поменять первую со второй, вторую с третьей, третью с первой, и т.д.
# Т.е. нужно вывести
# aaa
# aa
# a
# b
# bb
# bbb
# и так далее. Количество строк в файле может быть любым четным числом
# Результат записать в файл tmp/olymp-009-out.txt

# Подсказка
# - в задаче olymp-008 в range шаг 2, а тут 3


in_file = open('../data/olymp-009-in.txt', 'r')
str_list = []
for s in in_file:
    str_list.append(s)
in_file.close()
print(str_list)

for i in range(0, len(str_list), 3):
    a = str_list[i]
    b = str_list[i + 1]
    c = str_list[i + 2]
    str_list[i] = c
    str_list[i + 1] = b
    str_list[i + 2] = a
print(str_list)

out_file = open('../tmp/olymp-009-out.txt', 'w')
for s in str_list:
    out_file.write(s)
out_file.close()