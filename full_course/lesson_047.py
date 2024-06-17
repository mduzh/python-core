# Создать пустой список user_lst.
# Добавить в список пользователей admin, vadim и maxim.
# Распечатать user_lst и убедиться, что вывелось ['admin', 'vadim', 'maxim'].
user_lst = ['admin', 'vadim', 'maxim']
print(user_lst)

# Создать список mark_lst со значениями: 7, 9, 8, 5, 3, 1, 4, 10.
# Удалить последний элемент из списка используя pop.
# Распечатать mark_lst и убедиться, что вывелось [7, 9, 8, 5, 3, 1, 4].
mark_list = [7, 9, 8, 5, 3, 1, 4, 10]
mark_list.pop(-1)
print(mark_list)

# Удалить первый элемент из списка используя pop.
# Распечатать mark_lst и убедиться, что вывелось [9, 8, 5, 3, 1, 4].
mark_list.pop(0)
print(mark_list)

# Удалить первый элемент из списка используя pop и сохранить удаленны элемент в переменной deleted_mark.
# Распечатать deleted_mark и убедиться, что вывелось 9.
deleted_mark = mark_list.pop(0)
print(deleted_mark)

# Создать список price_lst со значениями: 1, 9, 8.
# Отсортировать список по возрастанию с помощью методы sort.
# Распечатать price_lst и убедиться, что вывелось [1, 8, 9].
price_lst = [1, 9, 8]
price_lst.sort()
print(price_lst)

# Отсортировать список по убыванию с помощью методы sort.
# Распечатать price_lst и убедиться, что вывелось [9, 8, 1].
price_lst.sort(reverse=True)
print(price_lst)
