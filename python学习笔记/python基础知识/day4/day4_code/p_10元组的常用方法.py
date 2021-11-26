'''
元组的常用方法
'''

t = (1, 2, 3, 4, 5, 6, 99, 323)
# 提示中方法名前面的 m 表示是一个方法， method：t.
print(t.count(2))
print(t.index(5))
print(t.index(2,3,8)) # ValueError: tuple.index(x): x not in tuple