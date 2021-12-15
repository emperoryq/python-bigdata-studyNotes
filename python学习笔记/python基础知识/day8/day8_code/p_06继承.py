'''
继承的实现
'''

# 定义一个父类
class Phone(object):

    def __init__(self):
        self.name = '电话'

    # 定义一个打电话的方法

    def call(self,number):
        print(f'正在给 { number} 打电话')



# 定义一个子类
class iPhone(Phone):

    # 添加一个拍照方法
    def carmera(self):
        print('正在拍照')


# 当发生继承后，子类会继承父类中的属性和方法，可以直接 使用

iphonex = iPhone()
iphonex.call('13800138000')
iphonex.carmera()
print(iphonex.name)

dgd = Phone()
dgd.call('13800138000')
print(dgd.name)
# dgd.carmera()