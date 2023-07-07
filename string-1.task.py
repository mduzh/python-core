#  теория тут: https://www.youtube.com/watch?v=pqaBWcsBGyA&list=RDCMUCCXF68Da_ndcmvv_9OG75Cw

# Дана строка s. Вывести на экран 3-й и 7-й символ строки (по индексу)
s = "Hello World!"
print(s[2])
print(s[6])
# Дана строка s. Вывести длину строки
s = "Hello World!"
print(len(s))
# Дана строка s. Посчитать количество букв l в строке
s = "Hello World!"
print(s.count('l'))
# Дана строка s. Вывести на экран строку в:
# - верхнем регистре ("HELLO WORLD!")
# - нижнем регистре ("hello world!")
# - Первая буква заглавная, а остальные маленькие ("Hello world!")
s = "Hello World!"
print(s.upper())
print(s.lower())
print(s.capitalize())
# Дана строка s. Вывести на эран все ли буквы в ней в верхнем регистре
s = "Hello World"
print(s.isupper())
# Дана строка s. Вывести на эран все ли буквы в ней в нижнем регистре
s = "hello world"
print(s.islower())
# Дана строка s. Найти индекс символа W в строке s и вывести на экран
s = "Hello World!"
print(s.find('W'))
# Дана строка s. Есть оли символ x в стрке s (использвать find)
s = "Hello World!"
# ERROR: ты ту выводишь -1, а не то, есть ли строка или нет. Подсказка: проверить, если = -1, то написать Нет, иначе написать Есть
print(s.find("x"))
# Дана строка s. Разделить строку на куски (split) и вывести на экран имена
s = "Denis, Vadim, Maxim"
print(s.split())
# Дана список имен. Объеденить имена в строку s с разделителем ", ". Распечатать s
ls = ["Denis, Vadim, Maxim"]
ls1 = ','.join(ls)
print(s.split(","))
# Дана строка s. С помощью среза получить кусок строки, что равен super. Результат сохранить в переменную res и распечатать
s = "I am super hero!"
print(s[5:10])