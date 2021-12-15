'''
烤地瓜
'''

# 抽象一个地瓜类
class SweetPotato(object):

    # 实现初始化方法，初始地瓜的状态和总烧烤时间
    def __init__(self):
        self.status = '生瓜蛋子'
        self.total_time = 0
        # 添加一个用来保存调料的容器属性
        self.condiments = []

    # 实现一个烧烤方法
    # 该方法有一个烧烤时间，这个时间会被累计到总时间上
    # 判断总时间，来改变地瓜状态
    def cook(self, t):
        # 累加时间
        self.total_time += t

        # 判断时间来改变地瓜状态
        # 0-3：生的，3-5：半生不熟，5-8烤好了，>8糊了
        if self.total_time < 3:
            self.status = '还是个生瓜蛋子'
        elif self.total_time < 6:
            self.status = '半生不熟'
        elif self.total_time < 8:
            self.status = '刚刚好，烤的冒油'
        elif self.total_time < 10:
            self.status = '烤糊了'
        else:
            self.status = '烤成碳了，直接烧火吧'

    # 添加一个加调料的方法
    def addCondiments(self, t1):
        # 将参数的调料保存起来就可以
        self.condiments.append(t1)

    # 实现__str__方法，定义地瓜的显示格式
    def __str__(self):
        s = self.status + f'被烤了{self.total_time}分钟'
        s += '地瓜使用了以下调料：\n'
        for i in self.condiments:
            s += (i + '\n')
        return s

# 测试
sp1 = SweetPotato()
print(sp1)

sp1.cook(2)
sp1.addCondiments('蜂蜜')
print(sp1)

sp1.cook(2)
sp1.addCondiments('老干妈')
print(sp1)

sp1.cook(2)
sp1.addCondiments('芥末')
print(sp1)

sp1.cook(5)
print(sp1)

sp2 = SweetPotato()
print(sp2)