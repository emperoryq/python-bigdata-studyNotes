'''类方法'''

class MyMath(object):

    # 定义一个类属性
    n = 999

    # 标准格式
    @classmethod  # 这是一个装饰 器，用来表示下面的方法是一个类方法
    def sum(cls,*args):
        print(cls.n)
        m = 0
        for i in args:
            m += i
        return m


    # @classmethod 是一个装饰 器，用来修饰一个方法成为类方法，当在执行该 类方法时，解释 会自动 将类对象传递到参数 cls中
    @classmethod
    def show(cls):
        print('show class method')

# 执行类方法
# print(MyMath.sum(1,2,3,4,5))
#
#
# mm = MyMath()
# print(mm.sum(1, 2, 3, 4, 5))

MyMath.show()