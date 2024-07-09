# В файле data/olymp-in.txt заданы 3 числа.
# Нужно сложить 2 первых числа и умножить на 3-е число.
# Результат записать в файл tmp/olymp-out.txt

file = open('../data/olymp-002-in.txt', 'r')
s1 = file.readline()
num1 = int(s1)
s2 = file.readline()
num2 = int(s2)
s3 = file.readline()
num3 = int(s3)
res = (num1 + num2) * num3
result = str(res)
file.close()

file1 = open('../tmp/olymp-002-out.txt', "w")
file1.write(result)
file.close()
