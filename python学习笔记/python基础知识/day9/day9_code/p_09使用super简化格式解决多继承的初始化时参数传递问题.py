'''
多继承的初始化问题的解决
'''

# 定义一个人类

class Person(object):
    def __init__(self,aaa):
        print('Person Init ...')
        self.aaa = aaa

class Father(Person):
    def __init__(self,name,*args):
        # super(Father, self).__init__(*args)
        super().__init__(*args)
        print('Father Init ...')
        self.name = name


class Mother(Person):
    def __init__(self,age,*args):
        # super(Mother, self).__init__(*args)
        super().__init__(*args)
        print('Mother Init ...')
        self.age = age


class Son(Father, Mother):
    def __init__(self,gender,name,age,aaa):

        # 参数二是当前类的实例对象
        # 参数一是当前类名
        # 在参数二对象的所属类的mro关系 中找参数一的下一个类进行实始化
        # super(Son, self).__init__(name,age,aaa)
        super().__init__(name,age,aaa)
        print('Son Init ...')
        self.gender = gender


# 测试
# s = Son(1, 'Tom',12,'男')
s = Son('男','Tom',12,1)
print(s.aaa)
print(s.name)
print(s.age)
print(s.gender)

print(Son.__mro__)
'''
这个顺序关系是解释器在执行代码 时，自动确认的我们无法干涉
(<class '__main__.Son'>,
 <class '__main__.Father'>, 
 <class '__main__.Mother'>, 
 <class '__main__.Person'>, 
 <class 'object'>)
'''


f = Father('Jack',2)
print(f.aaa)
print(f.name)
print(Father.__mro__)
