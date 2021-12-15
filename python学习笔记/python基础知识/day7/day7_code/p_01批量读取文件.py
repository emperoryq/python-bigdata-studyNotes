'''
批量读取文件，改名之后去复制

'''
# C:/Users/KG/Desktop/

# 因为要使用文件操作功能 ，所以要导入 os 模块
import os

def muilt_file_copy(src, dst):

    # 获取当前工作目录
    print(os.getcwd())
    # 切换目录 到 源文件目录中
    os.chdir(src)

    # 从源当中去读取所有的文件信息
    file_list = os.listdir(src)
    # print(file_list)

    # 创建出一个新的目标文件夹
    os.mkdir(dst)

    # 循环 读取文件次数
    # 遍历每一个文件
    for file in file_list:
        # 对文件改名，遍历的文件就是需要复制的源文件，改名后的文件就是要复制出来的文件
        # 先对源文件名进行分割
        s_file = file.rpartition('.')
        #　C:/Users/KG/Desktop/v_bak/v3_bak.mp4
        dst_file =  dst + '/' + s_file[0] + '_bak' + s_file[1] + s_file[2]
        print(dst_file)
        # print(dst_file)
        # 分别以读写方式打开源和目标文件
        file_r = open(file,'rb')
        file_w = open(dst_file,'wb')

        # 读取内容，写入内容
        while True:
            content = file_r.read(1024)
            #  因为打开文件时，使用的是二进制模式打开，所以在判断结束时，需要判断是否是一个二进制空字符串，b''
            if content == b'':
                print(f'{file} 复制成功。。')
                file_r.close()
                file_w.close()
                break
            # 如果读取内容不是空，将读取内容 写入到目标文件
            file_w.write(content)

    else:
        print(f'一共复制了{len(file_list)}个文件')





# 源文件夹
src = 'C:/Users/KG/Desktop/v'

# 目标文件夹
dst = 'C:/Users/KG/Desktop/v_bak'

# muilt_file_copy(src,dst)


a = [1,2,3]
b = map(lambda x: x* 10,a)

print(next(b))
print(next(b))
print(next(b))
print(next(b))

# for i in b:
#     print(i)
#
# for i in b:
#     print(i)
#
#
# a = (i for i in range(3))
# print(a)
#
# print(X(a))
# print(next(a))
# print(next(a))
# print(next(a))