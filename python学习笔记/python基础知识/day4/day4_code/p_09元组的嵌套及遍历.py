'''
元组的嵌套及遍历
'''

# 定义一个嵌套元组
t = (1, 2, 3, (4, 5, 6), (7, 8, 9))

# 遍历
for v in t:
    # isinstance() 判断参数一是否是参数二的类型对象
    # 通过 isinstance() 判断遍历的元素是否是一个元组，
    # 如果是就继续遍历，不是直接输出
    if isinstance(v, tuple):
        for v2 in v:
            print(v2)
    else:
        print(v)
