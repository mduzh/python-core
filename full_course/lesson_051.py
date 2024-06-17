# Создайте список car_lst с 5 элементами Mazda Honda Audi BMW Zeekr.
car_lst = ['Mazda', 'Honda', 'Audi', 'BMW', 'Zeekr']

# Удалите третий элемент.
# Распечатайте car_lst и убедитесь, что вывелось ['Mazda', 'Honda', 'BMW', 'Zeekr']
del car_lst[2]
print(car_lst)

# Выведите в терминал длину списка car_lst
# Убедитесь, что вывелось на экран 4.
print(len(car_lst))

# Поменяйте порядок следования элементов в списке на противоположное.
# Распечатайте car_lst и убедитесь, что вывелось ['Zeekr, 'BMW', 'Honda', 'Mazda']
car_lst.reverse()
print(car_lst)

# Создайте еще один список french_car_lst с двумя элементами 'Reno', 'Citroen'
french_car_lst = ['Reno', 'Citroen']

# Расширьте первый список car_lst элементами второго списка french_car_lst
# Распечатайте car_lst и убедитесь, что вывелось ['Zeekr, 'BMW', 'Honda', 'Mazda', 'Reno', 'Citroen']
car_lst.extend(french_car_lst)
print(car_lst)

# Выведите в терминал длину списка car_lst.
print(len(car_lst))

# Убедитесь, что вывелось на экран 6.


# Создайте два списка positive_nums со значениями 10, 20, 30 и negative_nums -1, -2, -3.
# Объедините два списка, используя оператор + и сохраните в переменной all_nums.
# Распечатайте all_nums и убедитесь, что вывелось [10, 20, 30, -1, -2, -3]
positive_nums = [10, 20, 30]
negative_nums = [-1, -2, -3]
all_nums = positive_nums + negative_nums
print(all_nums)