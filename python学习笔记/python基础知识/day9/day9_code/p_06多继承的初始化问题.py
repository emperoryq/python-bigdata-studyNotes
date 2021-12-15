'''
多继承的初始化问题
'''

# 定义一个人类
# 在这种 继承关系 上，这个共同的父类 Person 会被初台化多次，这是继承时的问题
# 是否 父类名调用 实始化方法的时候 引起的
class Person(object):
    def __init__(self,aaa):
        print('Person Init ...')
        self.aaa = aaa

class Father(Person):
    def __init__(self,aaa, name):
        Person.__init__(self,aaa)
        print('Father Init ...')
        self.name = name


class Mother(Person):
    def __init__(self,aaa, age):
        Person.__init__(self,aaa)
        print('Mother Init ...')
        self.age = age


class Son(Father, Mother):
    def __init__(self,aaa, name,age, gender):
        Father.__init__(self,aaa, name)
        Mother.__init__(self, aaa, age)
        print('Son Init ...')
        self.gender = gender


# 测试
s = Son(1, 'Tom',12,'男')
print(s.aaa)
print(s.name)
print(s.age)
print(s.gender)