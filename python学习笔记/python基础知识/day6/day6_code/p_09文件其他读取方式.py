'''
文件其他读取方式
'''

# 以行的形式读取文件

# 打开文件
file = open('a.txt', 'r')

# 以行读取readline()
# while True:
#     content = file.readline()
#     if content == '':
#         break
#     print(content, end='')

# 以行的方式读取文件 readlines()

content_list = file.readlines()
print(content_list)
for line in content_list:
    print(line)
    print(line.upper())

# 文件的写入
f1 = open('a.txt', 'wt')
content = 'test'
f1.write(content)

# 关闭文件
file.close()
f1.close()