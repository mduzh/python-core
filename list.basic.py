a = 1
a = 2

s = 'hello'
s = 'bye'

lst = []
num_list= [1, 3, 5]
str_list = ['hello', 'world']

print(str_list[1])

str_list[1] = 'good'

print(str_list[1])

num_list.append(0)
print(num_list)

l = len(num_list)
print(l)

# ===
print('--')
n0 = num_list[0]
print(n0)
n1 = num_list[1]
print(n1)
n2= num_list[2]
print(n2)
n3= num_list[3]
print(n3)

print('---')
for n in num_list:
    print(n)

print('----')
for index in range(4):
    print('start')
    print(index)
    n = num_list[index]
    print(n)
    print('end')

print('-4.2-')
list_length = len(num_list)
for index in range(list_length):
    n = num_list[index]
    print(n)

print('-5-')
for index in range(0, 4, 2):
    n = num_list[index]
    print(n)

print('-6-')
for index in range(1, 4, 2):
    n = num_list[index]
    print(n)

