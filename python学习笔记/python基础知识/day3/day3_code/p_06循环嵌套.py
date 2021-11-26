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
    j = 0
    while j < 5:
        print('j - ', j)
        j += 1
    i += 1