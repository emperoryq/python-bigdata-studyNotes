'''
__str__()方法
'''

class Cat(object):
    def __init__(self, name, age, height):
        # 将三个属性绑定给对象
        self.username = name
        self.age = age
        self.height = height

    # 默认没有实现__str__()方法，那么会打印 <模块名，类名，object as 0x...>
    # 如果想按自己的格式显示，需要再类中实现该方法
    def __str__(self):
        print('String Run..', self.username)
        # print(self.username, self.age, self.height)
        # 该函数必须有一个返回值
        # 并且这个返回值必须是一个字符串
        # 如果需要将对象的信息按照一定的格式进行格式化，那么可以再这里进行格式修饰
        # 修饰完后，可以将这个格式化字符串返回，让str()方法在执行时，得到该对象转换的字符串类型
        s = self.username.ljust(10) + str(self.age).ljust(5) + self.height.ljust(5)
        return s


tom = Cat('Tom', 1, '50cm')
jack = Cat('jack', 2, '50cm')
# print(tom.username)
# print(tom.age)
# print(tom.height)

print(tom) #<__main__.Cat object at 0x000001791818CFD0>
print(jack)

# c_list = list('hello')
#
# print(c_list)

tom_s = str(tom)
print('|' + tom_s + '|')