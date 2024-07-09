# - Пользователь вводит 3 числа и сохраняет в переменных a, b и c (не забудь про int())
# - Если a = b или a = c, тогда на экран выводим текст Есть совпадение
# - Иначе выводим Нет совпадения!

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a == b or b == c:
    print("Some similarities!")
else:
    print("No similarities!")