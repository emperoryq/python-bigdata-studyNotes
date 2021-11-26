'''
猜拳游戏
   a. 两个角色  玩家 player  - 电脑 robot
   b. 动作: 石头 0 , 剪刀 1,  布 2
   c. 我的出拳: 由输入完成
   d. 电脑的出拳: 随机数完成
   e. 比较出拳
   f. 相等 - 平局
   g. 玩家赢: p0:r1  p1:r2  p2:r0
   h. 剩下的情况就是电脑赢
'''

import random

def game(p, r):
    if p >= 0 and p <= 2:
        if (p == 0 and r == 1) or (p == 1 and r == 2) or (p == 2 and r == 0) :
            print(f'机器人出的动作：{r}')
            print('玩家出的动作：%s'%p)
            print('玩家赢')
        elif p == r:
            print(f'机器人出的动作：{r}')
            print('玩家出的动作：%s' % p)
            print('平局')
        else:
            print(f'机器人出的动作：{r}')
            print('玩家出的动作：%s' % p)
            print('机器人赢')
    else:
        print('玩家输入的动作不对，请重新输入')

p = int(input('请输入你想出的动作（石头 0 , 剪刀 1, 布 2）:'))
r = random.randint(0, 2)
game(p, r)

'''
思考题：输出机器人和玩家出的具体动作

升级题：棒子老虎鸡
    棒子->老虎->鸡->虫->棒子

扩展题：三局两胜，循环执行
'''