'''
全局变量和局部变量
'''

# 全局变量
num = 100

def func_a():
    # 定义一个局部变量
    a_num = 200
    print(a_num)

def func_b():
    # print(a_num)
    num = 300
    print(num)

# 变量查找规则
# LEGB
# Local -> EnClosed -> Global -> Buildins
# 本地 -> 闭包 -> 全局 -> 内建

func_a()
func_b()