'''
类的复合
练习：
人想听狗叫
'''

# 经过分析，应该设计两个类
# 一个人类，一个狗类

# 设计狗类
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self, n):
        for i in range(n):
            print('Won...')

# 设计一个人类
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 为人添加一个拥有宠物的方法
    def add_pet(self, pet):
        self.pet = pet

    # 人想听狗叫
    def listen_dog_bark(self, n):
        self.pet.bark(n)

# 测试
# 实例一个人类对象
tom = Person('TOM', 23)

# 为人的对象添加一条狗
tom.add_pet(Dog('golf', 1))

# 人调用想听狗叫的方法
tom.listen_dog_bark(3)

# jack = Person('jack', 22)
# jack.listen_dog_bark(5) # AttributeError: 'Person' object has no attribute 'pet'