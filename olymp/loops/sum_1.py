# Задача №320. Сумма - 1

# По данному числу n вычислите сумму 1+1/(2**2)+1/(3**2)+...+1/(n**2).
#
# Входные данные
# Вводится одно число n, не превосходящее 100000.
#
# Выходные данные
# Необходимо вывести  значение суммы.
#
# Примеры
# входные данные
# 2
# выходные данные
# 1.25

n = int(input("Enter your number: "))

res = 0
for value in range(1, n + 1):
    res = 1 + 1 / (value ** 2)
print(res)