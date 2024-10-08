# Задача №3069. Количество элементов, которые больше предыдущего
#
# Подсказка: Нужно сделать бесконечный цикл while. И читать ввод данных от пользователя. Если он ввел 0, тогда выходим
# из цикла. Если нет, то берем введенной число и с делаем то, что в задаче прописано.
#
# Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой
# последовательности больше предыдущего элемента.
#
# Числа, следующие за числом 0, считывать не нужно.
#
# Входные данные
# Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит).
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# Входные данные
# 1
# 7
# 9
# 0
# Выходные данные
# 2

prev_num = -1
total = 0
while True:
    num = int(input("Enter your number: "))
    if num == 0:
        break
    elif num > prev_num:
        if prev_num != -1:
            total += 1
        prev_num = num
print(total)
