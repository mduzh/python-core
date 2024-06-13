# Объявить функцию hello без параметров
# В блоке кода вызвать другую функцию print с параметром Hello there!
def hello():
    print('Hello there!')

    # Вызвать функцию hello
    hello()

    # Вызвать функцию hello дважды
    hello()
    hello()


# Объявить функцию hi с параметром name
# В блоке кода вызвать функцию print, которая печатает Hi, потом name, а потом !
# Затем вызвать функцию hi с параметром Vadim.
# Затем вызвать функцию hi с параметром Maxim.

def hi(name):
    print('Hi', name, '!')


hi('Vadim')
hi('Maxim')
