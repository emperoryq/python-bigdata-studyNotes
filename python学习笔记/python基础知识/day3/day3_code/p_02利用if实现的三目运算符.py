'''
if实现的三目运算符
'''

a = 1 if 3 > 2 else 0
print(a)

def test_func():
    n = int(input('number:'))

    s = '偶数' if n % 2 == 0 else '奇数'
    # ctrl + d 下一行复制

    return s

print(test_func())