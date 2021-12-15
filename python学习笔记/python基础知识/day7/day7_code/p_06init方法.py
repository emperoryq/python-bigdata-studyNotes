'''
__init__方法
该方法会在创建对象时自动调用
并对该对象进行初始化操作
'''

class Cat(object):
    # 实现魔法方法__init__，准备为对象初始化属性
    def __init__(self, name, age):
        print('Init Run ...', self)
        # 绑定属性时，使用 self.属性名 = 值
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

tom = Cat('tom', 1)
print(tom)

# 使用属性
print(tom.name)
print(tom.age)

jack = Cat('jack', 2)
print(jack)
print(jack.name)
print(jack.age)

# 在调用方法时，方法的第一个参数self是不用手动传参的
# 这个参数会由解释器自动将调用该方法的对象传递过去
tom.show()
jack.show()