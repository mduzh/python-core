# В файле data/olymp-004-in.txt заданы числа.
# Нужно перемножить все числа и результат записать в файл tmp/olymp-004-out.txt

file = open('data/olymp-004-in.txt', 'r')
res = 1
for i in file:
    res = res * int(i)
    print(res)

file.close()
