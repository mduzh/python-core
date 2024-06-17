# Дана переменная student_name. Преобразовать эту строку в список букв letter_lst.
# Распечатать letter_lst и убедиться, что вывелось ['J', 'o', 'h', 'n'].
student_name = "John"
letter_lst = list(student_name)
print(letter_lst)

# Даны два списка машин german_cars and japanese_cars.
# Объединить два списка и сохранить в переменной all_cars
# Распечатать all_cars и убедиться, что вывелось ['Audi', 'BMW', 'Mazda'].
german_cars = ["Audi", "BMW"]
japanese_cars = ["Mazda"]
all_cars = german_cars + japanese_cars
print(all_cars)

# Создать список mark_lst со значениями оценок учеников: 7, 9, 8, 10, 5, 6.
# Взять первые два элемента списка и сохранить в переменной first_lst.
# Распечатать first_lst и убедиться, что вывелось [7, 9].
mark_lst = [7, 9, 8, 10, 5, 6]
first_lst = mark_lst[:2]
print(first_lst)

# Взять 3 элемента списка, начиная со второго, и сохранить в переменной second_lst.
# Распечатать second_lst и убедиться, что вывелось [9, 8, 10].
second_lst = mark_lst[1:4]
print(second_lst)

# Взять 4 последних элемента списка, начиная со второго, и сохранить в переменной third_lst.
# Распечатать third_lst и убедиться, что вывелось [8, 10, 5, 6].
third_lst = mark_lst[2:]
print(third_lst)
