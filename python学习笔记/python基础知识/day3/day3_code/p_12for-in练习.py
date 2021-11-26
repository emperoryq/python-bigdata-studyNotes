'''
for-in 实现九九乘法表
'''

def nine_nine_table():
    # for i in range(1, 10):
    #     for j in range(1, i + 1):
    #         print('%dx%d=%-3d' % (j, i, j * i), end=' ')
    #     print()

    for i in range(1, 10):
        for j in range(1, 10):
            print('%dx%d=%-3d' % (j, i, j * i), end=' ')
            if i == j:
                break
        print()

nine_nine_table()