'''
__del__()方法

该方法用来在删除对象时，回收对象占的资源
'''

class Cat(object):
    def __init__(self, name):
        self.name = name


    def __del__(self):
        # 要在这个方法中将当前对象持有的其他对象手动销毁
        del self.name
        print('del run ...')

tom = Cat('tom')
# 执行下面的代码时，会自动调用 __del__ 方法，将这个对象销毁，回收对象内存资源
del tom
print('over')
# print(tom) # NameError: name 'tom' is not defined:tom对象已经被删除