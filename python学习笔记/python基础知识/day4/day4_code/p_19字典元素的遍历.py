'''
字典元素的遍历
'''

# 方式一
d = {'one':'星期一', 'two':'星期二', 'three':'星期三', 'haha':'周末'}

# 默认情况下，使用for-in遍历时，会将所有的key遍历出来
for k in d:
    print(f'{k} --> {d[k]}')

# 方式二
# keys()方法
print(d.keys()) # dict_keys(['one', 'two', 'three', 'haha'])
for k in d.keys():
    print(f'keys:{k} --> {d[k]}')

# 方式三
# values() 方法
print(d.values()) # dict_values(['星期一', '星期二', '星期三', '周末'])
for v in d.values():
    print(f'values:{v}')

# 方式四
# items()
print(d.items()) # dict_items([('one', '星期一'), ('two', '星期二'), ('three', '星期三'), ('haha', '周末')])
for item in d.items():
    print(f'items:{item[0]} --> {item[1]}')

for k, v in d.items():
    print(f'item:{k} --> {v}')

# 解包
item = (1, 2, 3, 4, 5)
a, b, c, d, e = item

print(a)
print(e)