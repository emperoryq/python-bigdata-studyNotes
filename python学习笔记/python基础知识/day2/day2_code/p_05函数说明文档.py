'''
函数说明文档，DocString
'''

def show():
    '''
    这是show函数的函数说明文档
    show 函数的作用是用来 显示一个字符串
    '''
    print('hello , world')


show()

help(show)

# 函数添加说明文档以后，可以使用help()函数显示说明文档，括号里面的函数不加括号

help(print) # 按住ctrl，点print 可以进去具体文档

