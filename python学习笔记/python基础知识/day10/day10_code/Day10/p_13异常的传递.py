'''
异常的传递
'''

def func_a():
    print('Func a run ...')
    func_b()


def func_b():
    print("Func b run ...")

    try:
        func_c()
    except Exception:
        print('你的除数为0了')


def func_c():
    print('Func c run ...')
    # try:
    #     print(1 / 0)
    # except Exception:
    #     print('你的除数为0了')

    print(1 / 0)



func_a()