# 方式一
# import p_05模块
#
# # 使用时，需要使用模块对象.成员
# print(p_05模块.n)
#
# p_05模块.show()
#
# tom = p_05模块.Cat()
# tom.show()

# 方式一的别名形式
# 别名就是为复杂的模块名起一个代号
# 可以通过这个代号 来调用 模块中的相应的成员

# import p_05模块 as p5m
# print(p5m.n)
# p5m.show()
# p5m.Cat().show()
# p5m.Cat().show()



# 方式 二
# 导入指定模块中的指定成员
# from p_05模块 import n
# from p_05模块 import show
# from p_05模块 import Cat as CatClass
#
# # 当使用from-import 方式 导入 时，不需要再使用 模块名.成员 形式
# # 可以在当前文件中，直接 使用成员名，相当于将导入的成功复制到了本地一份
# print(n)
# show()
# CatClass().show()


# 这两种 方式 的区别
# 使用import时，可以将整个模块中的成员 都 导入 进来
# 使用 from-import 时，可以使用谁导入谁，更加节省资源
# 如果想使用 From-import 方式 ，也可以导入所有的成员
# 如果使用通配符 * 的方式 导入所有的成员，那么就不能使用 as 为成员起别名了
from p_05模块 import *

print(n)
show()
Cat().show()

