'''
多层继承
'''

class A(object):
    def __init__(self, a):

        self.a = a


class B(A):
    def __init__(self,a,b):
        A.__init__(self, a)
        self.b = b

class C(B):
    def __init__(self,a,b,c):
        B.__init__(self,a,b)
        self.c = c


class D(C):
    def __init__(self,a,b,c,d):
        C.__init__(self,a,b,c)
        self.d = d


# 测试
d = D(1,2,3,4)
print(d.a)
print(d.b)
print(d.c)
print(d.d)


d.__dict__
D.__dict__
