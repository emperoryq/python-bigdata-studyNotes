'''
文件读取
'''

# 打开文件，以写模式
file = open('a.txt', 'rt')

# 读取文件内容
# 默认读取全部文件内容
# 但是这种方式只适用于 文件比较小的情况
# 如果文件比较大，不建议这样读取
# content = file.read()

# # 在读取数据时，指定读取一部分
# content = file.read(5)
#
# # 显示读取的文件内容
# print(content)

# 读取多行文件的方式
while True:
    # 读取
    content = file.read(4096)

    # 如果在文件读取时，读取的结果为空串，说明文件读取完毕
    # 根据 这个条件，可以设置读取文件的结束条件
    if content == '':
        break
    print(content, end='')

# 关闭文件
file.close()