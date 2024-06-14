# Создать переменную user_name и присвоить ей строковое значение admin.
# С помощью функции len посчитать длину строки user_name и сохранить ее в переменной name_len.
# Распечатать name_len и убедиться, что вывелось 5
user_name = 'admin'
name_len = len(user_name)
print(name_len)
# Создать переменную greeting и присвоить ей строковое значение Hello!
# Получить второй символ в строке greeting и сохранить ее в переменной letter_2.
# Распечатать letter_2 и убедиться, что вывелось e.
greeting = 'Hello!'
letter_2 = greeting[1]
print(letter_2)
# Получить пятый символ в строке greeting и сохранить ее в переменной letter_5.
letter_5 = greeting[4]

# Распечатать letter_5 и убедиться, что вывелось o.
print(letter_5)

# Распечатать последний символ в строке greeting и убедиться, что вывелось !.
print(greeting[-1])

# Распечатать второй символ с конца в строке greeting и убедиться, что вывелось o.
print(greeting[-2])

# Создать переменную message и присвоить ей строковое значение I am writing to greet you.
# Получить символы из строки message начиная с четвертого и заканчивая шестым. Сохранить ее в переменной sub_string.
# Распечатать строку sub_string и убедиться, что вывелось m w
message = 'I am writing to greet you'
# Распечатать часть строки message, начиная с начала и до 3-го символа включительно. Убедиться, что вывелось I a
print(message[:3])

# Распечатать часть строки message, начиная со 3-го символа и до конца. Убедиться, что вывелось am writing to greet you.
print(message[2:])

# Создать переменную text и присвоить ей строковое значение How are you?
# Перевести строку text в верхний регистр (большие буквы) с использованием метода upper и сохранить результат в upp_text
# Распечатать строку upp_text и убедиться, что вывелось HOW ARE YOU?
# Распечатать строку text и убедиться, что вывелось How are you? Т.е. старый текст не поменялся.
text = "How are you?"
upp_text = text.upper()
print(text)
print(upp_text)
# Распечатать строку text, чтобы все слова начинались с большой буквы (исп. capitalize).
print(text.capitalize())

# Распечатать строку text, чтобы в ней слова you заменились на they (исп. replace).
print(text.replace('you', 'they'))

# Посчитать сколько букв o в переменной text (исп. count) и сохранить результат в переменной o_count.
# Распечатать o_count и убедиться, что там 2.
o_count = text.count('o')
print(o_count)