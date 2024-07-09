# Дан файл file-4.in.txt в каталоге data, который содержит несколько строк
# Нужно вычитать все строки м переложить из в список str_list
# Распечатать str_list (просто через принт)

# Подсказки:
# - Можно посмотреть задачу №2 в file-2.task.py


file = open('../data/file-4.in.txt', 'r')
str_list = []
for s in file:
    str_list.append(s)
print(str_list,)
file.close()

