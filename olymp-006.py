# В файле data/olymp-006-in.txt заданы числа.
# Нужно найти максимальное число в файле, который содержит положительные числа,
# и результат записать в файл tmp/olymp-006-out.txt

# Подсказка
# - Можно взять за основу решение в olymp-003.py
# - Заводим переменную max_number, в которую записываем -1 (так как числа у нас в файле только отрицательные).
# - Проходим по циклу и проверяем: если число из файла больше чем max_number, то в max_number заносим то число,
# если нет, то ничего не делаем.
# - В конце в max_number будет максимальное число - его в tmp/olymp-005-out.txt вывести.


max_number = -1
file = open('data/olymp-006-in.txt', 'r')
for i in file:
    num = int(i)
    if num > max_number:
        max_number = num
print('max :', max_number)
file.close()


file1 = open('tmp/olymp-006-out.txt', "w")
r = str(max_number)
file1.write(r)

file1.close()