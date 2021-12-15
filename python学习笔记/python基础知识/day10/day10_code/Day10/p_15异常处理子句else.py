'''
异常处理子句，else 用来处理没有异常的的情况
'''


try:
    f = None
    f = open('b.txt','r')
except Exception as e:
    print('要打开的文件不存在')
    print(e)
else:
    # 对文件的读取操作
    print('else 是当没有出现异常时，执行的else语句 块')
    print(f.read())
finally:
    # 不管是否出现异常，都要执行这个语句块
    # 一般这个模块中，主要写的内容 是资料关闭或回收
    # 比如，文件的关闭，网络连接的关闭，数据库的关闭
    print('无论是否出现异常，都会执行finally语句 块')
    if f != None:
        f.close()



with open('a.txt','r') as f:
    print(f.read())

