'''
输出九九乘法表
'''

def nine_nine_table():
    # 外层循环用来控制行
    # i= 1
    # while i <= 9:
    #     # 内层循环用来控制 打印每一列的表达式
    #     j = 1
    #     while j <= i:
    #         print('%dx%d=%-3d' %(j, i , j * i), end = ' ')
    #         # print(f'{j} x {i} = {i * j}', end = ' ')
    #         j += 1
    #     print()
    #     i += 1

    i = 1
    while i <= 9:
        j = 1
        while j <= 9:
            print('%dx%d=%-3d' % (j, i, j * i), end=' ')
            if j == i:
                break
            j += 1
        print()
        i += 1

nine_nine_table()
