'''
子类初始化父类的属性
'''

# 父类
class Father(object):
    def __init__(self,name):
        print('Father Init Run ...')
        self.name = name


# 子类
class Son(Father):
    def __init__(self,name, age):
        #　因为子类提供了 init 方法后，那么在使用子类实例对象时，就会调用 子类自己 init 方法，
        # 那么就不会再调用 父类的init方法了，父类当中的属性就不会有绑定的机会，所以这时是没有父类的属性的
        # 如果想父类中的属性可以得到，需要执行父类中的init方法
        # 父类名.init()
        Father.__init__(self, name)
        print('Son Init run ..')
        self.age = age



# 测试
s = Son('Tom', 12)
print(s.name)
print('age:', s.age)

