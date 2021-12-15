'''
变量多态

python 中的变量（标识符），的类型是根据所代表的对象，进行自动推导得到的

'''


n = 1
print(type(n))

n =3.14
print(type(n))

n = True
print(type(n))

def show():
    print('show')

n = show
n()
print(type(n))