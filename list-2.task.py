# Вот тут можно посмотреть теорию: https://youtu.be/-X2ubBdP2Ak?list=RDCMUCCXF68Da_ndcmvv_9OG75Cw

# - Дан список. Вывести на экран каждый элемент списка используя цикл for
lst = [1, 2, 3, 4, 5]
for element in lst:
    print(element)

# - Дан список. Вывести на экран каждый элемент списка используя цикл while
lst = [10, 20, 30, 40, 50]
index = 0
while index < len(lst):
    print(lst[index])
    index += 1

# - Дан список. Вывести на экран каждый элемент списка умноженный на 10 используя цикл for
lst = [1, 2, 3, 4, 5]
for element in lst:
    element = element * 10
    print(element)

for index in range(len(lst)):
    element = lst[index] * 10
    print(element)

# - Дан список. Вывести на экран каждый элемент списка умноженный на 10 используя цикл while
lst = [10, 20, 30, 40, 50]
index = 0
while index < len(lst):
    print(lst[index] * 10)
    index += 1

# - Дан список. Вывести на экран те элементы списка, которые меньше 5.
# - Используем цикл for для прохода по списку и if для проверки
lst = [10, 2, 3, 7, 6]
for element in lst:
    if element < 5:
        print(element)

