# Сложить 2 числа.

# Числа задаются в файле data/olymp-001-in.txt
# - считать с файла первое число в переменную s1, используя функцию readline
# - считать с файла второе число в переменную s2, используя функцию readline

# - преобразовать s1 в число num1
# - преобразовать s2 в число num2

# - сложить числа num1 и num2 и сохранить переменной res
# - преобразовать res в строку s

# - записать s в файл tmp/olymp-001-out.txt

# - зайти в файл tmp/olymp-001-out.txt и проверить результат

file = open('data/olymp-001-in.txt', 'r')

s1 = file.readline()
num1 = int(s1)
s2 = file.readline()
num2 = int(s2)
res = num1 + num2
s = str(res)
file.close()


file = open('tmp/olymp-001-out.txt', 'w')
file.write(s)
file.close()