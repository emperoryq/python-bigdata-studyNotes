'''
在模块中，定义三个变量
'''

# 通过 __all__ 这个魔法属性 可以改变from-import 的导入规则
# 一般不会在这里去使用 __all__ 属性
# __all__ = ['_y', '__z']

x = 1       # 全局变量，模块间的公有变量
_y = 2      # 私有变量，文件内私有变量
__z = 3     # 私有变量，一般出现在类中，不在直接 在模块中定义，这里只是借用

