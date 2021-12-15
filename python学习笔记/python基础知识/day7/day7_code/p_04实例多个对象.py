'''
实例多个对象
'''

# 抽象一个人类

class Person(object):
    # 第一个方法
    def eat(self, food):
        print('一个人在吃', food)

    # 第二个方法
    def sleep(self, t):
        print('一个人睡了', t, '个小时')

# 实例对象
tom = Person()
jack = Person()
rose = Person()

# 实例对象时，会在内存中分配一块内存空间，这个空间就是这个对象的位置
# 然后将这个地址引用返回给对象名
print(tom)
print(jack)
print(rose)

# 使用对象来执行类中的方法
tom.eat('苹果')
tom.sleep(10)

jack.eat('土')
jack.sleep(2)

rose.eat('满汉全席')
rose.sleep(10)