# Написать свой модуль greeting (файл greeting.py)
# В модуле greeting реализовать функцию say_hello, которая принимает параметр name и возвращает "Hello " + имя + "!"
# Подключить модуль greeting и вызвать say_hello с параметром "John". Результат сохранить в переменную s
# Вывести s на экран
print("=== Start ===")
import greeting as gr

print(gr.name)
gr.say_hello()