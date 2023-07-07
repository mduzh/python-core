# Дан сет s. Добавить значение 4 и распечатать.
print("= START =")
s = {1, 2, 3}
s.add(4)
print(s)
# Дан сет s. Добавить значение 3
# Распечатать.
# Убедиться, что 3 не добавилось по второму разу
print("= START =")
s = {1, 2, 3}
s.add(3)
print(s)
# Дан сет s. Добавить значение 3 и 4 через update
# Распечатать.
# Убедиться, что 3 не добавилось по второму разу, а 4 добавилось, т.е. получили {1,2,3,4}
print("= START =")
s = {1, 2, 3}
s.update([3, 4])
print(s)
# Дан сет s. Удалить значение 2. Распечатать.
print("= START =")
s = {1, 2, 3}
s.remove(2)
print(s)
# Дан сет s. Удалить первое значение. Распечатать.
print("= START =")
s = {1, 2, 3}
s.pop()
print(s)
# Дан сет s. Удалить все значения. Распечатать.
print("= START =")
s = {1, 2, 3}
s.clear()
print(s)
