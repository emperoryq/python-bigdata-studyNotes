'''
实现一个单任务程序
'''

# 导入包
import multiprocessing
import time



# 制定任务函数
def task1():
    for i in range(10):
        print('A -- ',i+1)
        time.sleep(0.5)



def task2():
    for i in range(10):
        print('B -- ',i+1)
        time.sleep(1)



if __name__ == '__main__':
    # 创建子进程对象
    p1 = multiprocessing.Process(target=task1)
    p2 = multiprocessing.Process(target=task2)

    # 启动子进程
    p1.start()
    p2.start()