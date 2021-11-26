'''
列表的定义和下标访问
'''

# 定义一个空列表
cl1 = []
print(cl1)
print(type(cl1))

# 定义一个具有一个元素的列表
cl2 = [1]
print(cl2)
print(type(cl2))

# 定义具有多个元素的列表
cl3 = [1, 2, 3, 'hello', (4, 5, 6), ['a', 'b', 'c']]
print(cl3)
print(type(cl3))

for v in cl3:
    if isinstance(v, tuple) or isinstance(v, list) or isinstance(v, str):
        for i in v:
            print(i)
    else:
        print(v)

# 使用list()创建列表对象
# cl4 = list() # 空列表
cl4 = list('hahaha')
print(cl4)
print(type(cl4))

# 通过下标访问列表中的元素
cl5 = [1, 2, 3, 4, 5]
print(cl5[0])
print(cl5[3])
print(cl5[4])
# print(cl5[10]) # IndexError: list index out of range

# 重点：列表的特性，可以通过下标修改对应位置上的数据
print(cl5)
cl5[0] = 999
print(cl5)

# 字符串逆序
s = 'hello'

def revers_str(s):
    # 定义一个空字符串，用来拼接
    ret_s = ''
    i = len(s) - 1
    while i >= 0:
        ret_s += s[i]
        i -= 1

    return ret_s

print(revers_str(s))

print(s[::-1])