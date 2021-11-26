'''
使用全局变量共享数据
'''

# 全局变量
num = 0

c_list = []

t_tuple = (1,)

# 定义一个用来上传数据的函数
def upload_data():
    # print(num) UnboundLocalError: local variable 'num' referenced before assignment
    # 如果想修改全局变量，需要声明(不可变类型需要声明)
    global num, t_tuple

    num = 100
    print(num)
    c_list.append(1)
    t_tuple = (1, 2)


# 定义一个用来下载数据的函数
def download_data():
    print(num,c_list, t_tuple)

# 测试
download_data()
upload_data()
download_data()