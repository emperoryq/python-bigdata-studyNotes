'''
类对象和类属性
'''

class ClassRoom(object):
    # 当定义一个类属性时，相当于这个类中的全局变量
    # 该类的所有对象都 可以使用该 类属性
    # 可以在所有的对象间进行数据共享
    center_kong_tiao = '格力空调'


    # 实例方法
    def show(self):
        print('实例方法中去访问类属性：')
        print(ClassRoom.center_kong_tiao)



cr901 = ClassRoom()
print(cr901.center_kong_tiao)

cr902 = ClassRoom()
print(cr902.center_kong_tiao)

cr903 = ClassRoom()
print(cr903.center_kong_tiao)

# cr901.center_kong_tiao = '海尔空调'
ClassRoom.center_kong_tiao = '海尔空调'
print(cr901.center_kong_tiao)
print(cr902.center_kong_tiao)
print(cr903.center_kong_tiao)

cr901.show()


