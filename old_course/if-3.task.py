# - Пользователь вводит 3 числа и сохраняет в переменных a, b и c (не забудь про int())
# - Если a = b и b = c, тогда на экран выводим текст Все числа равны
# - Иначе выводим 3 числа не совпадают.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a == b and b == c:
    print("All numbers are equal!")
else:
    print("They are not equal!")
