'''
增：
	append()
	extend()
	insert()
'''

# append 追加数据
cl = []
cl.append(1)
cl.append(2)
cl.append(3)
cl.append('hello')
print(cl)
cl.append(['a', 'b'])
print(cl)

# extend() 扩展
# 可以将参数中的容器对象中的每个元素添加扩展到源列表中
cl1 = [1, 2, 3]
cl2 = ['a', 'b', 'c', [5, 6]]
# cl1.append(cl2)
cl1.extend(cl2)
print(cl1)

# insert 插入
cl3 = [1, 2, 3, 4, 5]
cl3.insert(0, 999)
print(cl3)
cl3.insert(2, 888)
print(cl3)
cl3.insert(7, 777)
print(cl3)

# 注意：在插入数据时，没有下标越界问题
# 如果指定下标超过元素正常范围，相当于追加
cl3.insert(17, 666)
print(cl3)