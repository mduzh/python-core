# Задача №1415. Шифр Юлия
#
# Юлий Цезарь использовал свой способ шифрования текста. Каждая буква заменялась на следующую по алфавиту через K
# позиций по кругу. Необходимо по заданной шифровке определить исходный текст.
#
# Входные данные
# В первой строке дана шифровка, состоящая из заглавных латинских букв. Во второй строке число K (1 ≤ K ≤ 10).
#
# Выходные данные
# Требуется вывести результат расшифровки.
#
# Примеры
# входные данные
# XPSE
# 1
# выходные данные
# WORD
# входные данные
# ZABC
# 3
# выходные данные
# WXYZ

encoded_text = input("Enter your cipher: ")
k = int(input("Enter the amount of rounds: "))

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

decoded_text = ""
for c in encoded_text:
    c_ind = letters.index(c)
    new_ind = (c_ind - k) % 26
    decoded_text = decoded_text + letters[new_ind]

print(decoded_text)
