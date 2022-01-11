'''
线程间共享全局变量时的资源竞争问题
'''

import threading
import time

# 全局变量,用来保存最后的累加和的变量
sum = 0

def add_num():
    global sum
    for i in range(1000000):
        sum += 1

    t = threading.current_thread()
    print(f'{t.name} 的计算结果是{sum}')


if __name__ == '__main__':
    t1 = threading.Thread(target=add_num)
    t2 = threading.Thread(target=add_num)

    t1.start()
    t2.start()


    time.sleep(3)
    print('Main:',sum)