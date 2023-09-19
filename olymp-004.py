# В файле data/olymp-003-in.txt заданы числа.
# Нужно сложить все числа и результат записать в файл tmp/olymp-003-out.txt

# Подсказка
# - заводим переменную со значением 0, в которой будет храниться результат
# - читаем каждую строку из файла (используем for - см. file-1.task.py в конце)
# - переводим прочитанную строку в число и добавляем к результату

res = 0

file = open('data/olymp-003-in.txt', 'r')
for s in file:
    value = int(s)
    res = res + value
file.close()

file = open('tmp/olymp-003-out.txt', "w")
file.write(str(res))
file.close()
