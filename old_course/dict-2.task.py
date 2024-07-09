# Дан словарь car. Вывести словарь car на экран
#
print("= START =")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
# Дан словарь car. Вывести на экран год выпуска с использованием []
#
print("= START =")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car["year"])
# Дан словарь car. Вывести на экран название производителя машина (brand) с функции get
#
print("= START =")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("brand"))
# Дан словарь car. Изменить в нем год выпуска на 1970 и вывести car на экран
#
print("= START =")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car['year'] = 1970
print(car)
# Дан словарь car. Добавить ключ fuel со значением "gasoline" и вывести car на экран
#
print("= START =")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car['fuel'] = 'gasoline'
print(car)
# Дан словарь car. Удалить ключ brand и вывести car на экран
#
print("= START =")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("brand")
print(car)
# Дан словарь car. Удалить ключ brand (использовать pop) и вывести car на экран
#
print("= START =")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("brand")
print(car)
# Дан словарь car. Удалить ключ year (использовать popitem) и вывести car на экран
#
print("= START =")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car)
# Дан словарь car. Удалить все ключи (использовать clear) и вывести car на экран
#
print("= START =")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)
