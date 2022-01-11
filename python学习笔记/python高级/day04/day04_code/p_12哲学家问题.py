'''
哲学家死锁问题
'''

import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def person_a():
    for i in range(100):
        lock_a.acquire()
        print('A 加第一个锁,抢到第一根筷子')
        lock_b.acquire()
        print('A 加第二个锁,抢到第二根筷子,吃一口饭')
        lock_b.release()
        print('A 释放第二个锁,放下第二根筷子')
        lock_a.release()
        print('A 释放第一个锁,放下第一根筷子')



def person_b():
    for i in range(100):
        lock_b.acquire()
        print('B 加第一个锁,抢到第一根筷子')
        lock_a.acquire()
        print('B 加第二个锁,抢到第二根筷子,吃一口饭')
        lock_a.release()
        print('B 释放第二个锁,放下第二根筷子')
        lock_b.release()
        print('B 释放第一个锁,放下第一根筷子')

# def call_func():
#     return person_b
#
#
# if __name__ == '__main__':
#     pa = threading.Thread(target=call_func())

if __name__ == '__main__':
    pa = threading.Thread(target=person_a)
    pb = threading.Thread(target=person_b)
    pa.start()
    pb.start()
