'''
break和continue这两个关键字不能用在循环以外的代码中
'''

# if True:
    # break
    # ontinue

n = 0
while True:
    n += 1
    print(n)
    if n == 3:
        break