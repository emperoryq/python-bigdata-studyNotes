'''
线程间可以共享全局变量
'''

import threading
import time


c_list = []

def add_data():
    for i in range(5):
        c_list.append(i)
        print(c_list)
        time.sleep(0.5)


def read_data():
    print("read: ", c_list)


if __name__ == '__main__':
    add_t = threading.Thread(target=add_data)
    read_t = threading.Thread(target=read_data)

    add_t.start()
    read_t.start()

    # 运行时,由于线程的执行顺序无法控制,有可能先去执行读取线程,那么这时读取出来的数据 是空
    # 这是正常的