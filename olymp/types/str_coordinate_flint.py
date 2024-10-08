# Задача №111. Капитан Флинт

# Капитан Флинт зарыл клад на Острове сокровищ. Он оставил описание, как найти клад. Описание состоит из строк вида:
# "North 5", где  слово – одно из "North", "South", "East", "West", – задает направление движения,
# а  число – количество шагов, которое необходимо пройти в этом направлении.
#
# Напишите программу, которая по описанию пути к кладу определяет точные координаты клада, считая, что начало координат
# находится в начале пути, ось OX направлена на восток, ось OY – на север.
#
# Входные данные
# На вход подается последовательность строк указанного формата. Гарантируется, что числа не превосходят 108
# .
#
# Выходные данные
# Необходимо вывести координаты клада – два целых числа через пробел. Гарантируется, что эти числа не превосходят 108.
#
# Примеры
# входные данные
# South 19
# выходные данные
# 0 -19


coordinates = input("Enter the coordinates of the treasure: ")

coordinates_list = coordinates.split()
coordinates_int = int(coordinates_list[1])

if coordinates_list[0] == "North":
    print(0, coordinates_int)
elif coordinates_list[0] == "South":
    print(0, coordinates_int * -1)
elif coordinates_list[0] == "East":
    print(coordinates_int, 0)
elif coordinates_list[0] == "West":
    print(coordinates_int * -1, 0)
