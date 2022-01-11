'''
获取进程ID和进程的父ID,进程名
'''

# 导入包
import multiprocessing
import time
import os

# 创建任务
def task1():
    # 获取当前进程对象
    mp = multiprocessing.current_process()
    print('task1:', mp)
    print(f"任务1的PID:{os.getpid()}  父进程的PID是{os.getppid()}")
    time.sleep(1)


def task2():
    # 获取当前进程对象
    mp = multiprocessing.current_process()
    print('task2:', mp)
    print(f"任务2的PID:{os.getpid()}  父进程的PID是{os.getppid()}")
    time.sleep(1)


if __name__ == '__main__':
    print(f"主进程的PID:{os.getpid()}  父进程的PID是{os.getppid()}")

    # 获取当前进程对象
    mp = multiprocessing.current_process()
    print(mp)
    print(mp.name)

    # 创建子进程
    p1 = multiprocessing.Process(target=task1,name='P1')
    p2 = multiprocessing.Process(target=task2,name='P2')

    print(p1)
    print(p2)

    # 启动进程
    p1.start()
    p2.start()

    print(p1)
    print(p2)


