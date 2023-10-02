# В файле data/olymp-003-in.txt заданы числа.
# Нужно сложить все числа и результат записать в файл tmp/olymp-003-out.txt


# Подсказка
# - заводим переменную со значением 0, в которой будет храниться результат
# - читаем каждую строку из файла (используем for - см. file-1.task.py в конце)
# - переводим прочитанную строку в число и добавляем к результату

file = open('data/olymp-003-in.txt', 'r')
res = 0
for num in file:
    res = res + int(num)

print(res)
file.close()

file1 = open('tmp/olymp-003-out.txt', "w")
r = str(res)
file1.write(r)

file1.close()
