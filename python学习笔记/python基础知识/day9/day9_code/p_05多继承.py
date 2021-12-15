'''
多层继承：纵向
多继承： 横向

'''

# 定义一个父亲类
class Father(object):
    def func_fa(self):
        print('Father Function ...')


# 定义一个母亲类
class Mother(object):
    def func_mo(self):
        print('Mother function ...')


# 上面的两个类，有一个共同子类
class Son(Father, Mother):
    def play(self):
        print('Son play...')

        
# 测试
s = Son()
s.play()
s.func_fa()
s.func_mo()