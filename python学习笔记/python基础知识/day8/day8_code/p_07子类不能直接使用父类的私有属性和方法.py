'''
子类不能直接使用父类的私有属性和方法
'''

class Father(object):
    def __init__(self):
        self.__money = 999
        self.name = 'tom'


    def __show(self):
        print('这个是父类中的一个私有方法')

    def display(self):
        print('这是一个父类中的公有方法')
        self.__show()



# 定义一个子类
class Son(Father):
    # 定义一个自己的方法
    def play(self):
        print('这是子类中玩的方法')
        # 在子类中不能直接使用父类中的私有方法
        # self.__show()
        # 通过继承得到的父类的公有方法，间接 执行父类的私有方法
        self.display()


# 测试

s = Son()
s.play()
s.display()
# s.__show()