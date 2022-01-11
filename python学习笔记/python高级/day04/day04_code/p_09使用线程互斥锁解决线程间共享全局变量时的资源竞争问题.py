'''
使用线程互斥锁解决线程间共享全局变量时的资源竞争问题
'''

import threading
import time


# 实例一个锁对象
metax_lock = threading.Lock()
# 为了能让锁起作用
# 一般会将这个锁加到对共享数据资源进行操作的代码上

# 全局变量,用来保存最后的累加和的变量
sum = 0

def add_num():
    t = threading.current_thread()

    global sum
    # 加锁
    metax_lock.acquire()

    for i in range(1000000):
        sum += 1
        print(t.name, ' -- ', sum)

    # 解锁
    metax_lock.release()

    print(f'{t.name} 的计算结果是{sum}')


if __name__ == '__main__':
    t1 = threading.Thread(target=add_num)
    t2 = threading.Thread(target=add_num)

    t1.start()
    t2.start()


    time.sleep(3)
    print('Main:',sum)