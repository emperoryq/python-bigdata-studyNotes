'''
多态
'''

# 标准多态

class Father(object):
    def cure(self):
        print('老中医使用中医治病')


class Son(Father):
    def cure(self):
        print('小大夫使用中西医结合治病')


class Dog(object):
    def bark(self):
        print('Won won ...')


class AnimalDoctor(object):
    def cure(self):
        print('我是个兽医，主要给动物治病，但是也能给人凑合治一下')


# 病人类
class Person(object):
    # 需要一个大夫给他治病
    def need_doctor(self,doctor):
        doctor.cure()


# 测试
p = Person()

p.need_doctor(Father())
p.need_doctor(Son())
# p.need_doctor(Dog())
p.need_doctor(AnimalDoctor())