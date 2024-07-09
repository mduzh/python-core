# Вот тут можно посмотреть теорию: https://youtu.be/-X2ubBdP2Ak?list=RDCMUCCXF68Da_ndcmvv_9OG75Cw&t=1276

# - Пользователь вводит число с экрана и сохраняем значение в переменную num.
# - Создать список.
# - Используя функцию append добавить в список элементы 0, 1, 2, ..., num -1
# - Вывести список на экран
# Code...
num = int(input("Enter the number: "))
lst = []
for i in range(0, num):
    lst.append(i)
print(lst)

# - Пользователь вводит число с экрана и сохраняем значение в переменную num.
# - Создать список.
# - Используя функцию append добавить в список элементы 0, 1 * 10, 2 * 10, ..., (num -1) * 10
# - Вывести список на экран
# Code...
num = int(input("Enter the number: "))
lst = []
for i in range(0, num):
    lst.append(i * 10)
print(lst)

# - Дан список lst.
# - Создать 2 новых списка lst1 и lst2
# - lst1 содержит числа меньше 10
# - lst2 содержит числа больше 10
# - вывести lst1 и lst2 на экран.
lst = [1, 10, 2, 3, 20, 30]
lst1 = []
lst2 = []
for i in lst:
    if i < 10:
        lst2.append(i)
    else:
        lst1.append(i)
print(lst1, lst2)

# - Дан список lst. Сложить первые 3 элемента в списке и добавить результат в lst
# Подсказка:
# - используем переменную total
# - Проходим по первым 3-м элементам lst и складываем в total
# - добавляем total в конец lst
total = 0
lst = [1, 2, 3, 4, 5]
for i in range(0, 3):
    total = total + lst[i]
lst.append(total)
print(total)


# - Дан список lst. Заменить первые 3 элемента на их сумму
# Подсказка:
# - После того, как посчитаешь total надо удалить первые 3 элемента
# - Потом вставить (insert) в начало списка значение total (т.е. [6, 4, 5])
total = 0
lst = [1, 2, 3, 4, 5]

for i in range(0, 3):
    total = total + lst[i]

for i in range(0, 3):
    lst.pop(0)

lst.insert(0, total)
print(lst)
