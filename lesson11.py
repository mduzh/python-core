# def test_func(word):
#     print(word, end="")
#     print('!')
#
#
# test_func("Hi")


# def summa(a, b):
#     # res = a + b
#     return a + b
#
#
# res = summa(4, 6)
# print(res)
#

def min_num(lst):
    minim = lst[0]
    for el in lst:
        if el < minim:
            minim = el

    print(minim)


num1 = [1, 2, 4, 5, 0]
min_num(num1)

