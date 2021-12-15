'''
两种导入 模块方式的区别
'''
# import p_06模块 as p6m
#
# print(p6m.x)
# print(p6m._y)
# print(p6m.__z)


# from p_06模块 import *
# print(x)
# 在使用这种 方式 导入 时，不会将私有的属性导入
# print(_y)
# print(__z)


# from -import 方式 的命令冲突问题

def x():
    print('x Function')


from p_06模块 import *
# x = 1




print(x)
x()


