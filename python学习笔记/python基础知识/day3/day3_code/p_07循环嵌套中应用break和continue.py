'''
循环嵌套
'''

'''
外层循环循环3次
内层循环循环5次
'''

i = 0
while i < 3:
    print('i - ', i)
    # break
    continue
    j = 0
    while j < 5:
        print('j - ', j)
        # break会跳出最近的所在的循环
        break
        j += 1
    i += 1