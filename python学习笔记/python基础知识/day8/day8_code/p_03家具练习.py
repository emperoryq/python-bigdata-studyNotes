'''
类的复合练习
向房子中添加家具
'''

# 设计一个家具类
class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'{self.name} 占用了 {self.area} 平米'

# 设计一个房子类
class House(object):
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = self.area * 0.3
        # 定义一个用来保存家具的容器属性
        self.furnitures = []

    # 实现一个添加家具的方法
    def add_furniture(self, fur):
        # 先判断剩余面积是否够添加到房中
        if fur.area < self.free_area:
            self.furnitures.append(fur)
            self.free_area -= fur.area
            print(f'添加了{fur}剩余空间还有{self.free_area}平米')
        else:
            print('空间不够，无法添加新家具')

    # 实现显示方法
    def __str__(self):
        s = f'我的大House在{self.address}，占地面积{self.area}平米\n'
        s += '家具如下:\n'
        # 遍历家具信息，拼接到房子信息后
        if len(self.furnitures) == 0:
            s += '还没有添加家具'
            return s
        else:
            for f in self.furnitures:
                s += (str(f) + '\n')
        return s

# 测试
home = House('长安街1号', 100)
print(home)

# 添加家具
bed1 = Furniture('双人床', 5)
home.add_furniture(bed1)
print(home)

home.add_furniture(Furniture('单人床', 3))
home.add_furniture(Furniture('饭桌', 4))
home.add_furniture(Furniture('椅子1', 1))
home.add_furniture(Furniture('椅子2', 1))
home.add_furniture(Furniture('椅子3', 1))
home.add_furniture(Furniture('椅子4', 1))
home.add_furniture(Furniture('大衣柜', 10))

home.add_furniture(Furniture('书桌', 10))
print(home)
