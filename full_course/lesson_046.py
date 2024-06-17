# #########################################################
# Список - это УПОРЯДОЧЕННАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ ЭЛЕМЕНТОВ
#
# - У каждого из элементов есть свой ИНДЕКС.
# - Индексы начинаются с 0.
# #########################################################


# Создать переменную user_lst и присвоить ей список, который содержит пользователей admin, vadim и maxim.
# Распечатать user_lst и убедиться, что вывелось ['admin', 'vadim', 'maxim'].
user_lst = ['admin', 'vadim', 'maxim']
print(user_lst)

# Создать переменную mark_lst, который содержит оценки на экзамене: 9, 8, 8 и 10.
# Распечатать mark_lst.
mark_lst = [9, 8, 8, 10]
print(mark_lst)

# Создать переменную student_data, который содержит имя, фамилию и возраст для человека John Doe 35 лет.
# Распечатать student_data.
student_data = ['John', 'doe', '35 лет']
print(student_data)

# Создать переменную empty_lst, который содержит пустой список.
# Распечатать empty_lst.
empty_lst = []
print(empty_lst)

# Есть 3 переменные microsoft, google и facebook
# Создать переменную company_lst, который содержит 3 переменные microsoft, google и facebook.
# Распечатать company_lst.
microsoft = "Microsoft"
google = "Google"
facebook = "Facebook"
company_lst = [microsoft, google, facebook]
print(company_lst)

# Создать переменную name_lst и присвоить ей список, который содержит пользователей John, Monica and Mike.
# Посчитать длину списка name_lst и сохранить результат в переменную names_len.
# Распечатать names_len и убедиться, что вывелось 3.
name_lst = ['John', 'Monica', 'Mike']
names_len = len(name_lst)
print(names_len)

# Создать переменную student_lst, который содержит Andrew, Ted, Ann и Alex.
# Получить первый элемент списка и сохранить его переменную student_name
# Распечатать student_name. Убедиться, что выведется Andrew
student_lst = ['Andrew', 'Ted', 'Ann', 'Alex']
student_name = student_lst[0]
print(student_name)

# Распечатать имя третьего студента.
# Убедиться, что это будет Ann
print(student_lst[2])

# Распечатать имя последнего студента.
# Убедиться, что это будет Alex.
print(student_lst[-1])

# Распечатать имя третьего с конца студента.
# Убедиться, что это будет Ted.
print(student_lst[-3])

# Создать переменную phone_lst, который содержит Nokia, IPhone, Samsung и Xiaomi.
# Поменять второй элемент списка, записав туда One Plus
# Распечатать phone_lst. Убедиться, что выведется ['Nokia', 'One Plus', 'Samsung', 'Xiaomi']
phone_lst = ['Nokia', 'Iphone', 'Samsung', 'Xiaomi']
phone_lst[1] = 'One Plus'
print(phone_lst)

# Поменять второй элемент с конца списка, записав туда Sony
# Распечатать phone_lst. Убедиться, что выведется ['Nokia', 'One Plus', 'Sony', 'Xiaomi']
phone_lst = ['Nokia', 'One Plus', 'Samsung', 'Xiaomi']
phone_lst[-2] = 'Sony'
print(phone_lst)

# Создать переменную car_lst, который содержит Honda, Mazda, Zeekr и Audi.
# Удалить второй элемент списка.
# Распечатать car_lst. Убедиться, что выведется ['Honda', 'Zeekr', 'Audi']
car_lst = ['Honda', 'Mazda', 'Zeekr', 'Audi']
del car_lst[1]
print(car_lst)

# Удалить первый элемент списка.
# Распечатать car_lst. Убедиться, что выведется ['Zeekr', 'Audi']
del car_lst[0]
print(car_lst)
