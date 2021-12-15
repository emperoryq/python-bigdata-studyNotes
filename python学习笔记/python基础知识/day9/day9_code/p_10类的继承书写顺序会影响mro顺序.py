'''
类的继承书写顺序会影响mro顺序
'''

class A(object):
    pass

class B(A):
    pass

class C(A):
    pass

# class D(B,C):
# (<class '__main__.D'>, < class '__main__.B' >, < class '__main__.C' >, < class '__main__.A' >, < class 'object' > )

class D(C,B):
# (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
    pass


print(D.__mro__)