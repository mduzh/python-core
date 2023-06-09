# - Пользователь вводит на возраст и сохраняет как число (num функция) в переменной age
# - Проверить age и вывести на экран, можно ли продавать спиртное.

age = int(input("Enter your age: "))
if age < 18:
    print("You will not get an alcohol!")
else:
    print("You can get an alcohol!")
