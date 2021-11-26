'''
列表的排序和逆序
'''

cl = [9, 2, 5, 7, 1, 8, 4, 3, 0, 6]

print(cl)

# 排序 默认升序排序（从小到大）
print(cl.sort()) # None， sort()函数无返回值，默认None
print(cl)

cl = [9, 2, 5, 7, 1, 8, 4, 3, 0, 6]
# 降序排序（从大到小）
cl.sort(reverse=True)
print(cl)

# 逆序
cl = [9, 2, 5, 7, 1, 8, 4, 3, 0, 6]

# 逆序是直接将原列表中的顺序进行逆转
cl.reverse()
print(cl)

# 实现列表逆序方法
def reverse_list(cl):
    # 定义一个空列表
    ret_1 = []
    i = len(cl) - 1
    while i >= 0:
        ret_1.append(cl[i]) # s += c
        i -= 1
    return ret_1

print(reverse_list(cl))
