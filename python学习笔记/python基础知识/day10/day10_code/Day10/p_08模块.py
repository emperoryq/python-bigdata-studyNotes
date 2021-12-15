
n = 1

def show():
    print('show')


class Cat(object):
    def show(self):
        print('Cat_show')


# 在当前文件下测试成员的使用

# 当使用 __name__ 属性在获取当前模块名时，会有两种 效果
# 如果当前模块文件是  主动执行 时，__name__ 得到的结果是字符串 __main__ 表示这是程序的入口
# 如果当前模块文件是  被动执行 时（被别人导入时），__name__　得到的结果就是当前模块文件的文件名
print('name:', __name__)

if __name__ == '__main__':
    print(n)
    show()
    Cat().show()

