'''
函数的嵌套调用
    嵌套调用是指，在一个被调用的函数体内又调用了另外一个函数
'''

# 定义三个函数
def func_a():
    print('Func A Start...')
    func_b()
    print('Func A Stop...')

def func_b():
    print('Func B Start...')
    func_c()
    print('Func B Stop...')

def func_c():
    print('Func C Start...')
    print('Func C Stop...')

# 执行函数调用
func_a()