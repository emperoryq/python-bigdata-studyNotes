'''
子类重写父类中的方法
'''

# 父类
class Father(object):
    # 实现一个治病
    def cure(self):
        print('父类是个老中医，使用中医古法治病')


# f = Father()
# f.cure()

# 子类
class Son(Father):
    # 子类也是一个大夫，也有治病的功能
    def cure(self):
        # 直接使用 父类名.方法名 形式来引用父类的功能
        Father.cure(self)
        print('子类出国深造，学成以后，使用中西医结合方法治病')


s = Son()
s.cure()
