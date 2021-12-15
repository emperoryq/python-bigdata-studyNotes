# import cn.itcast.web.a as weba1
# print(weba1.m)
#
# from cn.itcast.web import a as weba2
# print(weba2.m)
#
# from cn.itcast.web.a import *
# print(m)

# 想直接导入这个 web 包
# 在这里，如果只导到包的位置，那么通过 这个包去找模块时，会报错，因为不确定要导入哪个模块
# 需要在包中的 __init__.py 中，告诉解释器，当导入包时，应该导入哪些模块
# import cn.itcast.web as web
# print(web.a.m)
# print(web.b.n)


# from cn.itcast import web
# print(web.a.m)
# print(web.b.n)



# 小结：
'''
当在使用 import 方式 ，或from-import 方式 导入包时，
需要在 __init__.py 文件中，明确的指出可以被导入的模块有哪些
使用 from . import 模块名 形式指定 
如果在该 文件中没有指定 可以导入的模块时，默认不导入任何模块
'''

import cn.itcast.web as web
print(web.a.m)

from cn.itcast.web import *
print(a.m)
print(b.n)

