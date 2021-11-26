'''
字典练习（名片管理）
	函数一: 建立名片-> 建立好的名片
	函数二: 显示名片-> 接收谁打印谁
'''

# 定义字典的函数
def creat_card():
    # 使用字典来保存每张名片的数据
    # name, age , adddress
    card = {}
    card['name'] = input('请输入姓名：')
    card['age'] = input('请输入年龄：')
    card['address'] = input('请输入地址：')

    return card

# 显示字典内容的函数
def show_card(card):
    for k in card:
        print(f'{k}:{card.get(k)}')

# 测试
show_card(creat_card())