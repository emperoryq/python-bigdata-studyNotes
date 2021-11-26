'''
字典的增删改查
'''

d = {}

# 增
# 如果在赋值时，使用的key在字典中不存在，那么就是向字典中添加数据
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 3
d['e'] = 3
print(d)

# 改
# 如果在赋值时。使用的key在字典中存在，那么就修改这个key所对应的数据
# 注意：
# 字典中的key具有唯一性
# 如果key不存在，那么就是添加数据，如果存在就是修改数据
# key是不能修改的
d['a'] = 11
print(d)

# 查
print(d['a'])
print(d.get('a'))

# 删除
# popitem 删除最后一个键值对
# d.popitem()
# print(d)
# d.popitem()
# print(d)

# pop(key)
# pop 可以通过key来删除任意位置的键值对
print(d)
d.pop('c')
print(d)

# 清空字典中的键值对
# d.clear()
# print(d)

# del
del d['e']
print(d)

del d
# print(d) NameError: name 'd' is not defined