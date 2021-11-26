'''
学生管理系统
    print("----------------------")
    print("     学生管理系统V1.0")
    print("1：添加学生)
    print("2：删除学生)
    print("3：修改学生)
    print("4：查询学生)
    print("5：显示所有学生)
    print("6：退出系统)
    print("----------------------")

程序分析：
    1.学生怎么表示
    2.学生可能使用 学号id， 姓名name， 年龄age，可以使用一个字典来表示每一个学生
    3.应该有一个容器去保存所有的学生字典，可以使用列表实现
    4.应该有一个 主控函数
    5.菜单函数
        5-1.选择功能的函数
    6.添加学生函数
    7.修改学生函数
    8.查找学生
    9.删除学生
    10.显示所有学生的函数
    11.因为创建学生和修改学生，都需要从键盘输入数据，那么输入数据这个功能可以提取出一个函数，返回输入的数据
    12.添加一个功能函数，用来显示每个学生的信息
'''

# 定义一个学生的列表，用来保存来管理学生

students = []

# 主控制函数
def main():
    # 通过死循环控制程序可以重复运行
    # 显示菜单
    while True:
        show_menu()
        # 键盘输入选择一个功能
        select_id = input('请输入一个功能ID：')
        # 根据输入调用相应的功能
        operator(select_id)

# 菜单函数实现
def show_menu():
    print("----------------------")
    print("     学生管理系统V1.0")
    print("1：添加学生")
    print("2：删除学生")
    print("3：修改学生")
    print("4：查询学生")
    print("5：显示所有学生")
    print("6：退出系统")
    print("----------------------")

# 功能 选择函数
# 参数是传递的用来选择的功能id
def operator(select_id):
    if select_id == '1':
        add_stu()
    elif select_id == '2':
        del_id = input('请输入一个要删除的学生ID：')
        del_stu(del_id)
    elif select_id == '3':
        modify_id = input('请输入一个要修改的学生ID：')
        modify_stu(modify_id)
    elif select_id == '4':
        query_id = input('请输入一个要查询的学生ID：')
        search_stu_with_id(query_id)
    elif select_id == '5':
        show_all_info()
    elif select_id == '6':
        exit(0) # 程序通过exit()方法,可以直接结束
    else:
        print('输入的ID错误，请重新输入')

# 实现一个输入函数
# 用来从键盘获取学生信息，并返回
def input_stu_info():
    # 保存输入的学生信息
    stu_id = input('请输入学号：')
    stu_name = input('请输入姓名：')
    stu_age = input('请输入年龄：')
    # 同时返回多个数据时，会组包成一个元组
    return stu_id, stu_name, stu_age

# 实现添加函数
def add_stu():
    # 主体思路就是向列表中添加一个字典
    # 创建一个学生字典，空的
    stu = {}
    # 调用输入函数，获取学生信息
    stu_info = input_stu_info()
    # 利用获取的信息为字典添加数据
    stu['id'] = stu_info[0]
    stu['name'] = stu_info[1]
    stu['age'] = stu_info[2]

    # 将字典加到列表中
    students.append(stu)

    print(students)

# 实现学生查找的功能
# 返回被找到的学生
def search_stu_with_id(stu_id):
    # 遍历每个学生
    for stu in students:
        # 判断学生是否是查找到的人
        if stu['id'] == stu_id:
        # 找到返回该学生
            show_stu_info(stu)
            return stu

    # 返回没找到
    else:
        print(f'学号为{stu_id}的学生不存在')
        return None

# 实现一个用来显示单个学生信息的函数
def show_stu_info(stu):
    print(f"学号：{stu['id']} 姓名：{stu['name']} 年龄：{stu['age']}")

# 实现删除学生的函数
def del_stu(del_id):
    # 找到要删除的学生
    stu = search_stu_with_id(del_id)
    # 从列表中删除
    if stu != None:
        students.remove(stu)

# 实现修改学生的函数
def modify_stu(modify_id):
    # 查找学生
    stu = search_stu_with_id(modify_id)
    # 如果找到就修改
    if stu != None:
        # 先去调用输入函数获取数据
        stu_info = input_stu_info()
        # 利用获取的信息为字典添加数据
        stu['id'] = stu_info[0]
        stu['name'] = stu_info[1]
        stu['age'] = stu_info[2]

# 显示所有学生信息
def show_all_info():
    # 遍历打印
    for stu in students:
        show_stu_info(stu)

# 执行函数，运行程序
main()