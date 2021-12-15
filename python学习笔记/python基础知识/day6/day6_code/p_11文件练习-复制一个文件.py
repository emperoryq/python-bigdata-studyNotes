'''
实现了一个复制命令
'''

# 导入一个模块
import sys

def file_copy(src, dst):
    # 以读的方式打开源文件
    file_r = open(src, 'r')
    # 以写的方式打开目标
    file_w = open(dst, 'w')
    # 循环
    while True:
        # 读取文件内容
        content = file_r.read(1024)
        # 将读取的文件内容 写入到另一个文件中
        if content == '':
            print('文件拷贝成功')
            break
        # 写入文件
        file_w.write(content)
    # 关闭文件
    file_r.close()
    file_w.close()

print(sys.argv)
src = sys.argv[1]
dst = sys.argv[2]
file_copy(src, dst)