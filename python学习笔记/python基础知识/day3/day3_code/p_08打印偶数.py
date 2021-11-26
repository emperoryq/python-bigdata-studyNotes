'''
打印偶数
'''

def print_even(n):
    i = 0
    while i < n:
        # if i % 2 == 0:
        #     print(i)
        i += 1
        if i % 2 == 1:
            continue
        print(i)

print_even(10)