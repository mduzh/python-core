# Задача №3074. Числа Фибоначчи
##
# Последовательность Фибоначчи определяется так:
#
# φ0=0,  φ1=1, φ2=φ1+φn0, φn3=φ2+φn1, ..., φn=φn-1+φn-2.
#
# По данному числу n определите n-е число Фибоначчи φn.
#
# Входные данные
# Вводится натуральное число n.
#
# Выходные данные
# Выведите ответ на задачу.
#
# Ввод	Вывод
# 6
# 8

n = int(input("Enter your number: "))

a = 0
b = 1
i = 2
while i <= n:
    f = a + b
    a = b
    b = f
    i += 1
print(f)


