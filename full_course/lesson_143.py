 # Используя if elif напиши программу, которая запрашивает у пользователя число и выводит, является ли оно положительным, отрицательным или равным нулю.

num = int(input("Enter a number: "))
if num > 0:
    print('Positive')
elif num < 0:
    print('Negative')
else:
    print('Zero')

# Напиши программу, которая запрашивает у пользователя номер месяца (от 1 до 12) и записывает в переменную season
# соответствующее время года (зима, весна, лето, осень).
# После выхода из if распечатать значение переменной season
season = int(input("Enter the number of a month: "))
if season == 1 or season == 2 or season == 12:
    print(season, 'Winter')
elif season == 3 or season == 4 or season == 5:
    print(season, 'Spring')
elif season == 6 or season == 7 or season == 8:
    print(season, 'Summer')
elif season == 9 or season == 10 or season == 11:
    print(season, 'Autumn')

# Напиши программу, которая запрашивает у пользователя два целых числа и выводит большее из них.
# Нужно учесть, что два числа могут быть равными.
num1 = int(input('Enter first number: '))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print('First number is bigger')
elif num2 > num1:
    print('Second number is bigger')
else:
    print('They are equal')

# Напиши программу, которая запрашивает у пользователя оценку (от 1 до 5) и выводит сообщение об успеваемости:
# "Отлично", "Хорошо", "Удовлетворительно", "Неудовлетворительно".
mark = int(input('Enter your mark: '))
if mark == 5:
    print('Отлично')
elif mark == 4:
    print('Хорошо')
elif mark == 4:
    print('Удовлетворительно')
elif mark == 2:
    print('Неудовлетворительно')
else:
    print('Плохо')

# Напиши программу, которая запрашивает у пользователя число и проверяет, находится ли оно в диапазоне от 1 до 100
 # включительно.

num_value = int(input('Enter your number: '))
if 1 <= num_value <= 100:
    print('Ok')
else:
    print('Your number is out of definite range')

 # Напиши программу, которая запрашивает у пользователя строку и проверяет, начинается ли она с буквы "а".
# У строки есть метод startswith, который говорит о том, начинается ли строка с указанной строки.
str1 = input('Enter something: ')
if str1.startswith('a'):
    print('Correct')
else:
    print('Not de1finite beginning')
# Напиши программу, которая запрашивает у пользователя пароль и проверяет, совпадает ли он с заранее заданным
# значением correct_password.
correct_password = "password123"
psw = input('Enter your password: ')
if psw == correct_password:
    print('Correct')
else:
    print('Wrong')