'''
	os 模块
	rename(）
	remove()
	mkdir()
	getcwd()
	chdir()
	listdir() 掌握
	rmdir()
'''

# 导入os模块
# os -> operator system -> 操作系统
import os

# rename 重命名
# os.rename('a.txt', 'b.txt')

# mkdir 创建目录 make directory
# 如果当前目录存在，会报错
# os.mkdir('test_dir')

# getcwd 获取当前工作目录 get current work directory
cwd = os.getcwd()
print(cwd)

# listdir() 获取当前目录下的文件列表
file_list = os.listdir('.')
print(file_list)
for file in file_list:
    print(file)

print('*' * 10)

# chdir() 改变当前目录到指定的路径上去 change directory
# os.chdir('C:\\Users\\Desktop')
# print(os.getcwd())
# print(os.listdir('.'))

# remove() 删除一个文件
# os.remove('aaa.txt')

# rmdir() 删除一个文件夹 remove directory
# 当目录不为空，不能删除
# os.rmdir('D:/python/DAY06/text_dir')