'''
进程注意事项2-主进程会待子进程结束后再结束

'''


import multiprocessing
import time


def task():
    for i in range(5):
        print('task -- ', i)
        time.sleep(0.5)



if __name__ == '__main__':
    p = multiprocessing.Process(target=task)
    p.start()

    print('Main Process Over')


