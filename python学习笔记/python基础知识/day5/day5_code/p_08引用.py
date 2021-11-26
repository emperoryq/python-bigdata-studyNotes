'''
引用的概念
'''

# 引用就是数据再内存中存储时的内存编号

# 通过 id() 函数可以得到数据在内存中的地址

print(id(1))
print(id(1))
print(id(1))

a = 1
print(id(1))
print(id(a))

b = a
print(id(1))
print(id(a))
print(id(b))
print('*' * 20)

a = 2
print(id(1))
print(id(2))
print(id(a))
print(id(b))
