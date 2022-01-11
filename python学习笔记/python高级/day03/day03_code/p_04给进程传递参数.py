'''
给进程传递参数
'''

import multiprocessing
import time

def task1(count):
    for i in range(count):
        print('task1 - ', i+1)
        time.sleep(1)



def task2(content, count):
    for i in range(count):
        print(content, ' - ', i+1)
        time.sleep(1)

if __name__ == '__main__':
    # 利用args传参
    p1 = multiprocessing.Process(target=task1, args=(5,))
    p2 = multiprocessing.Process(target=task2, args=('Python'), 5)

    # 利用kwargs传参
    # p1 = multiprocessing.Process(target=task1, kwargs={'count': 5})
    # p2 = multiprocessing.Process(target=task2, kwargs={'count': 5, 'content': 'Hello'})


    p1.start()
    p2.start()