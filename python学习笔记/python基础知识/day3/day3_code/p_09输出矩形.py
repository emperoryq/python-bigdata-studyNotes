'''
打印正方形
	* * * * *
	* * * * *
	* * * * *
	* * * * *
	* * * * *
'''

def print_rect():
    i = 1
    while i <= 5:
        j = 1
        while j <= 5:
            # 在print函数中，使用 end= 形式来给print函数设置一个结束符号，默认的结束符是 \n 换行符
            print('*', end=' ')
            j += 1
        print('\n')
        i += 1
print_rect()

def print_tringle():
    i = 1
    while i <= 5:
        j = 1
        while j <= i:
            print('*', end = ' ')
            j += 1
        print()
        i += 1

print_tringle()
