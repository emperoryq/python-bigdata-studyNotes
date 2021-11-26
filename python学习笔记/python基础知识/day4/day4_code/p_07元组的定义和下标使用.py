'''
元组的定义和下标的使用
'''

# 元组的定义

# 定义一个空元组
t1 = ()
print(t1)
print(type(t1))

# 定义包含元素的元组
t2 = (1, 2, 3, 4, 5)
print(t2)
print(type(t2))

# 定义包含其他数据类型的元组
t3 = ('a', 'b', 'hello', 'world')
print(t3)

# 元组的复杂定义形式
t4 = (1, 3.14, 'Hello', True, t3)
print(t4)

# 定义具有一个元素的元组，特殊，注意，重点
t5 = (1,)
print(t5)
print(type(t5))

# 使用类型名定义元组
t6 = tuple()
print(t6)

t7 = tuple('hello') # 参数为可迭代的数据类型
print(t7)

# 元组的下标访问
t8 = (1, 2, 3, 4, 5, 6, 7, 8)
print(t8[0])
print(t8[3])
print(t8[7])
# 元组也不能使用超出范围的下标，会出现越界错误
# print(t8[70]) # IndexError: tuple index out of range

# 元组是一种 不可变类型，不能修改元组中的元素，修改会报错
t8[0] = 1111 # TypeError: 'tuple' object does not support item assignment