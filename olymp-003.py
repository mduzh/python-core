# В файле data/olymp-003-in.txt заданы числа.
# Нужно сложить все числа и результат записать в файл tmp/olymp-003-out.txt


# Подсказка
# - заводим переменную со значением 0, в которой будет храниться результат
# - читаем каждую строку из файла (используем for - см. file-1.task.py в конце)
# - переводим прочитанную строку в число и добавляем к результату

file = open('data/olymp-003-in.txt', 'r')
res = 0
for num in file:
    result = res + int(num)
    print(result)
    res1 = str(result)

file1 = open('tmp/olymp-003-out.txt', "w")
file1.write(res1)

file1.close()
