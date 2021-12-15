'''
导入包中的模块
'''
# 导入 normal_dir 这个包中的 a 模块
# import normal_dir.a
# print(normal_dir.a.m)

# import normal_dir.a as nda
# print(nda.m)


# 使用from-import 方式导入
# 从  normal_pack 包中导入 b 模块
# 使用时，需要指定包名. 成员
# from normal_pack import b
# print(b.n)


# 从 normal_pack的 b 模块中，导入 b 模块中的所有成员
from normal_pack.b import *
print(n)