'''
线程任务参数
'''

# 1. 导模块
import threading
import time

# 2. 实现任务函数
def task1(count):
    for i in range(count):
        print('Hello -- ', i+1)
        time.sleep(0.5)


def task2(content, count):
    for i in range(count):
        print(content, ' -- ', i+1)
        time.sleep(0.5)


# 创建线程
if __name__ == '__main__':
    # # 方式一 通过 arsg 传入元组来为多任务传参
    # t1 = threading.Thread(target=task1,args=(5,))
    # t2 = threading.Thread(target=task2,args=('Python',5))

    # 方式二 通过 kwarsg 传入字典来为多任务传参
    t1 = threading.Thread(target=task1, kwargs={'count': 5})
    t2 = threading.Thread(target=task2, kwargs={'count': 5, 'content': 'World' })
    t1.start()
    t2.start()