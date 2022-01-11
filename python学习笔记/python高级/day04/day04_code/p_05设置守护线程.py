'''
设置守护线程
'''

import threading
import time

def task():
    # 打印线程名
    t = threading.current_thread()

    for i in range(5):
        print(t.name)
        time.sleep(0.5)


if __name__ == '__main__':
    # 无守护线程状态
    # t1 = threading.Thread(target=task)
    # t2 = threading.Thread(target=task)


    # # 设置守护线程的方式一
    # t1 = threading.Thread(target=task, daemon=True)
    # t2 = threading.Thread(target=task, daemon=True)

    # 设置守护线程的方式二
    t1 = threading.Thread(target=task)
    t2 = threading.Thread(target=task)

    t1.setDaemon(True)
    t2.setDaemon(True)


    t1.start()
    t2.start()
    print('Main Over')