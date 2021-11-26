'''
访问字典中的元素
'''

d = {'one':'星期一', 'two':'星期二', 'three':'星期三', 'haha':'周末'}
print(d)

# 字典也是通过下标方式来访问元素，但是字典中没有索引，也就是没有下标编号
# 字典通过下标的中括号中书写key的方式来直接访问key所对应的值
print(d['one'])
print(d['two'])
print(d['haha'])
# print(d['hahaha']) KeyError: 'hahaha' 访问时，如果使用了不存在的key，会报错

# 字典也是一个可变类型
d['haha']='星期日'
print(d)