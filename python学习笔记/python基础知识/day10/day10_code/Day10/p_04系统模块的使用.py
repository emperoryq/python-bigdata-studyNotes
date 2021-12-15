'''
系统模块的使用
'''

import os
import time
import sys

print(os.getcwd())

# sleep 函数是一个time模块中定义的函数，用来让程序休眠，这是一个阻塞函数
time.sleep(3)
print('over')

# sys.argv 变量用来接收命令行参数
print(sys.argv)

