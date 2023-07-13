# Метериалы тут: https://www.youtube.com/watch?v=t-xQAhLNYSs&list=PLDyJYA6aTY1lPWXBPk0gw6gR8fEtPDGKa

# Открыть файл text.txt и затем закрыть его
file = open('text.txt', 'w')
file.close()
# Открыть файл text.txt в каталоге data и затем закрыть его
file = open('data/text.txt', 'w')
file.write('hello')
file.write('World')
file.close()
# Создать файл text.txt в каталоге tmp.
# - не забыть его закрыть после создания
# - для проверки зайти в PyCharm в каталог tmp и найти там файл text.txt
file = open('tmp/text.txt', 'w')
file.close()
# Создать файл write.txt в каталоге tmp и записать в него "Hello"
# - не забыть его закрыть после создания
# - для проверки зайти в PyCharm в каталог tmp и найти там файл write.txt. Открыть и увидеть в файле "Hello"
file = open('tmp/write.txt', 'w')
file.write('Hello')
file.close()
# Создать файл append.txt в каталоге tmp и записать в него "Hello" и закрыть его.
# Открыть файл append.txt в каталоге tmp для добавления и записать в него "World!" и закрыть его.
# - для проверки зайти в PyCharm в каталог tmp и найти там файл append.txt. Открыть и увидеть в файле Hello World!
file = open('tmp/append.txt', 'a')
file.write('Hello ')
file.write('World')
file.close()
# Прочитать весь файл text.txt в каталоге data и сохранить его содержимое в переменную s.
# Распечатать s (Должно быть Hello World !)
# Закрыть файл
file = open('data/text.txt', 'r')
print(file.read())
file.close()
# Прочитать 4 символа из файла text.txt в каталоге data и сохранить его содержимое в переменную s.
# Распечатать s (Должно быть Hell)
# Закрыть файл
file = open('data/text.txt', 'r')
print(file.read(4))
file.close()
# Прочитать каждую строку из файла text.txt в каталоге data и вывести ее на экран (использовать for)
# Распечатать s (Должно быть Hello World !)
# Закрыть файл
file = open('data/text.txt', 'r')
for s in file:
    print(s)
file.close()
