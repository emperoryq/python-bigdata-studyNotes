'''
无论是 for-in-else
还是   while-else
都是在执行完循环后，正常结束后，执行else后的代码
'''

def for_in_else():
    for i in range(5):
        print(i)
        if i == 3:
            print('找到了3')
            break
    else:
        print('over')

for_in_else()

def while_else():
    i = 0
    while i < 3:
        print(i)
        if i == 3:
            print('找到了3')
            break
        i += 1
    else:
        print('while over')

while_else()