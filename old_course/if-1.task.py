# - Пользователь вводит 2 числа и сохраняет в переменных a и b (не забудь про int())
# - Если a > b, тогда на экран выводим текст a больше b, иначе выдоим a меньше b

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
if a > b:
    print("Number a is bigger!")
else:
    print("Number b is bigger!")
