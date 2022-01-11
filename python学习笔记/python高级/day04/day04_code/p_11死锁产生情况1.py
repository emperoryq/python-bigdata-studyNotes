'''
死锁产生的情况1
'''

import threading

c_list = [1,2,3]

# 创建一个锁
lock = threading.Lock()


def get_value(index):

    # 加锁
    lock.acquire()

    t = threading.current_thread()

    # 加个判断用来解决下标越界问题
    if index >= len(c_list):
        print(f'{index} 下太大,导致下标越界')
        # 因为下标的问题,应该在结束该线程之前,将这个锁给释放掉
        lock.release()
        return

    print(t.name ,'取得第', index, '个值,值为',c_list[index])

    # 解锁
    lock.release()

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=get_value, args=(i,))
        t.start()