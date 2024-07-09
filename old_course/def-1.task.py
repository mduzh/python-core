# Написать функцию func1, которая ничего не делает (т.е. пустая). Использовать pass
# Вызвать функцию func1
print("=== START ===")


def func1():
    pass


func1()
# Написать функцию func2, которая печатает Hello World! (использовать print внутри функции)
# Вызвать функцию func2
print("=== START ===")


def func2():
    print("Hello world!")


func2()
# Написать функцию func3, которая принимает параметр name и печатает Hello, а потом то, что передается в name
# Вызвать функцию func3 с параметром John
print("=== START ===")


def func3(name):
    print("Hello", end=" ")
    print(name)


func3("John")
# Написать функцию func4, которая
# - принимает 2 параметра num1 и num2.
# - перемножает num1 на num2 и сохраняет результат в res
# - возвращает res
# Вызвать функцию func4 с параметрами (4, 5) и сохранить результат в переменной value
# Вывести на экран value (должно быть 20)
print("=== START ===")


def func4(num1, num2):
    res = num1 * num2
    return res


value = func4(4, 5)
print(value)
