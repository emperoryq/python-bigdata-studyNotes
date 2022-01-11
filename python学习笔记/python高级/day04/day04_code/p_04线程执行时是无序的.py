'''
线程执行时是无序的
'''

import threading
import time

def task():
    # 打印线程名
    t = threading.current_thread()

    for i in range(10):
        print(t.name)
        time.sleep(0.5)


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=task)
        t.start()


