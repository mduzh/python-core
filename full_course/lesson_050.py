# Дан список машин car_list.
# Посчитать, сколько раз встречается в списке автомобиль Audi и сохранить в переменную audi_count.
# Распечатать audi_count и убедиться, что вывелось 3.
german_cars = ['Audi', 'BMW', 'Opel', 'Mercedes', 'Audi', 'Audi']
audi_count = german_cars.count('Audi')
print(audi_count)

# Дан список телефонов phone_lst.
# Добавит в список телефон Xiaomi вторым элементом списка
# Распечатать phone_lst и убедиться, что вывелось ['IPhone', 'Xiaomi',  'Samsung'].
phone_lst = ['IPhone', 'Samsung']
phone_lst.insert(1, 'Xiaomi')
print(phone_lst)

# Дан список num_lst.
# Удалить все элементы списка.
# Распечатать num_lst и убедиться, что вывелось [].
num_lst = [10, 2, 17]
num_lst.clear()
print(num_lst)

# Даны два списка машин car_list and japanese_cars.
# Добавить japanese_cars в список car_list
# Распечатать car_list и убедиться, что вывелось ['Audi', 'BMW', 'Mazda'].
car_list = ["Audi", "BMW"]
japanese_cars = ["Mazda"]
car_list = car_list + japanese_cars
print(car_list)

# Дан список age_lst.
# Создать копию age_lst и сохранить в new_age_list
# Распечатать new_age_list и убедиться, что вывелось [16, 16, 23].
age_lst = [16, 16, 23]
new_age_list = list(age_lst)
print(new_age_list)




