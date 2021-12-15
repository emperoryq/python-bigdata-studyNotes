'''
扩展：属性和方法的保存位置
'''

class Cat(object):
    def __init__(self,name):
        self.name = name
        self.__age = 1

    def public_method(self):
        print('公有的对象方法')

    def __private_method(self):
        print('私有的对象方法')


tom = Cat('Tom')
jack = Cat('Jack')
# __dict__ 是一个魔法属性，用来保存当前对象的所有的成员
print(Cat.__dict__)
print(tom.__dict__)
print(jack.__dict__)

tom.public_method()

Cat.public_method(tom)
Cat.public_method(jack)

def display():
    print('Display')

display()


