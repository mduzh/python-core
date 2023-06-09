# - Пользователь вводит 2 числа и сохраняет в переменных a и b (не забудь про int())
# - Если a > b, тогда на экран выводим текст a больше b
# - Если a < b, тогда на экран выводим текст a меньше b
# - иначе выводим a равное b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("a bigger than b")
elif a < b:
    print('a less than b')
else:
    print("a equal to b")
