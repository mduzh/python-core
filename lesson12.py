# 'w' = rewrite info in file
# 'a' = appends info to current info
# data = input("Enter text: ")
# file = open('data/text.txt', 'a')
#
# file.write(data + '\n')
#
#
# file.close()


file = open('data/text.txt', 'r')

# print(file.read(10))
for line in  file:
    print(line)

file.close()
