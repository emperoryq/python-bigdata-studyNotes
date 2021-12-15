'''
设计一些类
类在python中分为旧式类（经典类）和新式类
'''

# 经典类
class Hero:
    # 定义一个方法：
    def skill(self):
        print('发一个大招。。。')

# 经典类2
class Person():
    # 定义两个方法
    def eat(self, food):
        print('吃', food)

    def sleep(self):
        print('每天至少睡8小时')

# 新式类
class Dog(object):
    def dark(self):
        print('Won Won...')

