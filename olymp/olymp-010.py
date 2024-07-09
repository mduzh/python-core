# В файле data/olymp-010-in.txt числа
# Нужно сложить все первые, вторые, третьи и четвертые цифры и результат (4 числа) записать в файл tmp/olymp-010-out.txt

# Подсказка
# - когда будешь из файла вычитывать и складывать в массив, то преобразуй строку в числj
# - заведи 4 переменные и в них накапливай сумму
# - используй задачу olymp-009, только там шаг 3, а у тут 4
# - когда будешь выводить числа в файл, то не забудь их перевести в строки

in_file = open('../data/olymp-010-in.txt', 'r')
num_list = []
for s in in_file:
    n = int(s)
    num_list.append(n)

in_file.close()
print(num_list)

res1 = 0
res2 = 0
res3 = 0
res4 = 0
for index in range(0, len(num_list), 4):
    a = num_list[index]
    b = num_list[index + 1]
    c = num_list[index + 2]
    d = num_list[index + 3]
    res1 = res1 + a
    res2 = res2 + b
    res3 = res3 + c
    res4 = res4 + d
print(res1 , res2, res3 , res4)

out_file = open('../tmp/olymp-010-out.txt', 'w')
out_file.write(str(res1))
out_file.write('\n')
out_file.write(str(res2))
out_file.write('\n')
out_file.write(str(res3))
out_file.write('\n')
out_file.write(str(res4))
out_file.write('\n')
out_file.close()