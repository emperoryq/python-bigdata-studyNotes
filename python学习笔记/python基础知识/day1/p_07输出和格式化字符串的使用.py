'''
格式化 字符串并输出
'''

# 占位符形式字符串
a = 10
print('现在要打印一个数字，值是%d' %a)

print('name:%s age:%d' %('tom',  12))

# 占位符的常用格式
print('%d' %1)
print('%5d' %1)
print('%05d' %1)
print('%-5d' %1)
print('%3d' % 12345) #12345

print('%.2f' % 3.1415926)
print('%.2f' %3.1) #3.10

# f_string
name = 'tom'
age = 11
print(f'name:{name} age:{age} score:{99}')

s = f'name:{name} age:{age} score:{99}' # 格式化字符串，不是必须和print配合
print(s)