'''
线程使用
'''

# 1. 导入模块
import threading
import time

# 实现多任务的功能函数

def task1():
    for i in range(5):
        print('Task A  ',i+1)
        time.sleep(0.5)



def task2():
    for i in range(5):
        print('Task B  ',i+1)
        time.sleep(0.5)


# 创建线程
if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    # 创建好线程后,线程并不会执行
    # 必须启动线程
    t1.start()
    t2.start()

    time.sleep(0.5)

    print('Main Thread')
