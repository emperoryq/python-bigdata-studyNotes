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

    # 方式二 设置守护进程
    # 注意: 设置进和时,需在开始进程之前设置
    p.daemon = True


    p.start()


    time.sleep(0.5)
    # 方式一
    # 在主进程结束之前,手动调用方法结束子进程
    # p.terminate()



    print('Main Process Over')


