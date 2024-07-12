# Напишите программу, которая запрашивает у пользователя список чисел, разделенных пробелами, и определяет, сколько
# из этих чисел являются четными и сколько нечетными.

# Сначала ввести строку и сохранить ее переменную numbers_str.
numbers_str = input('Enter a string: ')
# Затем разобрать строку numbers_str (использовать метод split) и сохранить результат в списке str_num_lst.
str_num_lst = numbers_str.split()
# Распечатать str_num_lst.
print(str_num_lst)
# Заводим 2 счетчика odd_count и even_count.
# Затем проходим по каждому элементу списка str_num_lst, где лежат числа как строки.
# И каждый элемент списка переводим в целое число int_value.
# Проверяем, является ли число четным (% возвращает 0), тогда увеличиваем счетчик четных чисел на 1.
# Иначе увеличиваем счетчик нечетных чисел на 1.
odd_count = 0
even_count = 0
for c in str_num_lst:
    int_value = int(c)
    if int_value % 2 == 0:
        even_count = even_count +1
    if int_value % 2 != 0:
        odd_count = odd_count + 1
print('even : ', even_count, 'odd : ',  odd_count)
# Выводим результат на экран. Убеждаемся, что если ввести 2 3 5, т будет 1 и 2. А если ввести 2 4 6, то будет 0 и 3
