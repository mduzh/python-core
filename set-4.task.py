# Дан список учеников, каждый элемент которого является словарем. С помощью set-а посчитать кол-во имен мальчиков в классе
# Подсказка:
# - создаем set с именем res, где будем складывать все имена
# - идем по списку. Каждый элемент списка - это словарь.
# - берем элемент, из него втаскивает значение по ключу firstName
# - сколько элеиентов в списке res, столько и имен - этио вывести на экран
print("= START =")
lst = [
    {"firstName": "Maxim", "lastName": "Duzh"},
    {"firstName": "Maxim", "lastName": "Petrov"},
    {"firstName": "Maxim", "lastName": "Ivanov"},
    {"firstName": "Vadim", "lastName": "Duzh"},
    {"firstName": "Vadim", "lastName": "Ivanov"},
    {"firstName": "Pavel", "lastName": "Pavlov"},
]
