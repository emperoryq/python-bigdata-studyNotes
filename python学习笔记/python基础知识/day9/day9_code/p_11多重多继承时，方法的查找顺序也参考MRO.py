'''
多重多继承时，方法的查找顺序也参考MRO
'''

class A(object):
    def show(self):
        print('A _ Show Run ...')


    def info(self):
        print('A - Info run ...')


class B(A):
    def show(self):
        print('B _ Show Run ...')

class C(A):
    def show(self):
        print('C _ Show Run ...')

    def info(self):
        # super().info()
        # A.info(self)
        print('C - Info run ...')



class D(B,C):
    def show(self):

        super().show()
        A.show(self)
        print('D _ Show Run ...')




d = D()
d.show()
d.info()