# В файле data/olymp-005-in.txt заданы числа.
# Нужно найти содержит ли файл отрицательное число. Если да, то записать 'Yes'  в файл tmp/olymp-005-out.txt,
# иначе записать 'No'

# Подсказка
# - Можно взять за основу решение в olymp-003.py
# - В переменную res занести значение 'No' - будем сразу считать что нет отрицательного числа.
# - В циклен проверяем является ли число отрицательным. Если да, тогда в переменную res заносим 'Yes' и ВЫХОДИМ из цикла
# - потом res записываем в tmp/olymp-005-out.txt

res = 'No'
file = open('../data/olymp-005-in.txt', 'r')

for s in file:
    num = int(s)
    print('num:', num)
    if num < 0:
        res = 'yes'
        break
print(res)

file.close()


file1 = open('../tmp/olymp-005-out.txt', "w")
r = str(res)
file1.write(r)

file1.close()