'''
多层继承
'''

class A(object):
    def a(self):
        print('a function')


class B(A):
    def b(self):
        print('b function')


class C(B):
    # C类中重写了B类中的方法
    def b(self):
        B.b(self)
        print('b in C function')


    def c(self):
        print('c function')


class D(C):
    def d(self):
        print('d function')


# 测试
d = D()
d.a()
d.b()
d.c()
d.d()
