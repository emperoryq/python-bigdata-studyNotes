'''
可变参数的二次传递
'''

def show(a, *args, **kwargs):
    print(a)
    print(args)
    # 出错原因，只把元组args传给了a
    # display(args) TypeError: display() missing 3 required positional arguments: 'b', 'c', and 'd'
    print(*args)
    display(*args) # *args手动解包，将元组中的元素依次赋给四个变量

def display(a, b, c, d):
    print(a, b, c, d)

show(1, 2, 3, 4, 5)