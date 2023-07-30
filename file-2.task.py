# Дан файл file-2.task.txt в каталоге data, который содержит числа, которые нужно сложить
# В первой строке - первое число, а во второй - второе, и так далее - сколько там строк мы не знаем
# Нужно посчитать сумма всех чисел в файле.
# Подсказки:
# - заводим переменную total, где будем хранить сумму
# - читаем каждую строку с помощью for (см. последнюю задачу из file-1.task.py) и сохраняем в переменную s
# - так как s строка, то нужно ее перевести в число и сохраняем в переменной n
# - добавляем n к total
# - выводим total на экран
total = 0
file = open('data/file-2.task.txt', 'r')
for line in file:
    n = int(line)
    total = total + n
print(total)
file.close()

# Дан файл file-2.task.txt в каталоге data, который содержит числа.
# В первой строке - это количество строк, что нужно сложить, а начиная со второй это складываемые числа
# Можно сделать так:
# - заводим переменную data, который является списком (сначала он пустой []). В этой переменной будем хранить все цифры
# - читаем каждую строку с помощью for (см. последнюю задачу из file-1.task.py) и сохраняем в переменную s
# - так как s строка, то нужно ее перевести в число и сохраняем в переменной n
# - добавляем n в список data
# - Выводим на экран список data
# - Первый элемент - это кол-во чисел, чтобы сложить
# - заводим переменную count и ей присваиваем первый элемент списка
# - Все остальные элементы - это числа, что будем складывать.
# - заводим переменную numbers типа список и ему присваиваем значения data начиная с 2 элемента и до конца (используй срезы)
# - заводим переменную total, где будем хранить сумму
# - проходим в цикле по списку numbers
# - добавляем каждый элемент списка к total
# - выводим total на экран

file = open('data/file-2.task.txt', 'r')
data = []
for s in file:
    n = int(s)
    data.append(n)
print(data)

count = data[0]
numbers = (data[1:])
print(numbers)
total = 0
for i in range(count):
    total = total + numbers[i]
print(total)
file.close()





