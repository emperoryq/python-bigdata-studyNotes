'''
实例属性和实例 方法
'''

class Cat(object):
    def __init__(self,name):
        # 定义一个实例 属性
        self.name = name


    # 定义了一个实例方法
    def info(self):
        print(self.name)

    def show(self):
        print('Show Run :')
        self.info()


# 测试
tom = Cat('Tom')
# 使用实例属性
print(tom.name)
# 使用实例方法
tom.info()
tom.show()


# Python中万物皆对象
# print(Cat.name)
Cat.show()

# 结论：
# 为什么类名不能调用 实例 对象属性和实例对象方法呢？
# 因为类对象存在时，不一定有实例对象存在
# 实例属性和实例 方法只能由实例对象调用


