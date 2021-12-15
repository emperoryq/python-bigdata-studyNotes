'''
注意：同时捕捉多个异常，但是同一时刻只能有一个异常发生
'''

try:
    # n = 1
    n / 0
# except (ZeroDivisionError,NameError) as e:
# except Exception as e:
except :
    print('出现异常了')

