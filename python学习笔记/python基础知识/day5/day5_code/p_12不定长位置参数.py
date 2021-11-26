'''
不定长位置参数,不定长关键字参数
'''

# 不定长位置参数
def my_sum(*args):
    print(args)
    sum = 0
    for i in args:
        sum += i
    print(sum)

my_sum(1, 2)
my_sum(1, 2, 3)
my_sum(1, 2, 3, 4)
my_sum(1, 2, 3, 4, 5)

# 不定长关键字参数
def my_sum(**kwargs):
    print(kwargs)

my_sum(a = 1, b = 2)
my_sum(a = 1, b = 2, c = 3)
my_sum(a = 1, b = 2, c = 3, d = 4)
my_sum(a = 1, b = 2, c = 3, d = 4, e =5)