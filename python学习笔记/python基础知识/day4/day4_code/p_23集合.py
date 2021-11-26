'''
集合的使用
'''

# 定义一个集合
s = {1, 2, 3, 4, 5, 6, 7, 7, 7}
print(s)
print(type(s))

# 定义一个空集合
# s = {} # 这种方式是定义一个空字典，不是集合
s = set() # 定义一个空集合的正确方式
print(s)
print(type(s))

s = {1, 2, 3, 4, 5, 6, 7, 7, 7}
for v in s:
    print(v)

# 注意：集合是不支持下标的
# print(s[0]) # TypeError: 'set' object is not subscriptable