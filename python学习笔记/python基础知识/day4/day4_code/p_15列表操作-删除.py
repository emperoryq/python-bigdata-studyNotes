'''
删：
	pop（）
	remove()
	clear() 清空但列表存在
	del 全没了
'''

cl = [1, 2, 3, 4, 5, 6, 7, 3, 7, 90, 91, 0]

# pop()
# pop 中的 index 参数可以不写，默认删除最后一个
cl.pop()
print(cl)

cl.pop(0)
print(cl)

# remove()
# 删除指定对象，当有多个相同对象时，只删除第一个
cl.remove(7)
print(cl)

# del 有两种方式
del cl[1]
print(cl)

del(cl[1])
print(cl)

# 将整个列表删除
#del cl
# print(cl) NameError: name 'cl' is not defined

# del(cl)
# print(cl) NameError: name 'cl' is not defined

# clear()
# 清空列表元素

cl.clear()
print(cl)

# 在使用列表时，不要在循环遍历时删除元素

cl = [2, 5, 6, 3, 7, 90, 91]

for o in cl:
    cl.remove(o)

print(cl)