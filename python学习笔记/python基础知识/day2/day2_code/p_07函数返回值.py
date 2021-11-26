'''
函数返回值
return
'''

def get_num():
    return 1

# print(get_num())
# 将一个函数返回值，赋值给一个变量
a = get_num()
print(a)

def show():
    print(1)
    print(2)
    return
    print(3)

show()
print('over')
print(show()) # return默认返回None

