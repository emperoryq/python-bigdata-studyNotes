'''
函数同时返回多个数据
    需求：求一个列表数据中的最大值和最小值
'''

def get_max_min():
    cl = [1, 0, 3, 5, 2, 6, 8, 7, 4, 9]
    # ma = max(cl)
    # mi = min(cl)

    cl.sort()
    ma = cl[len(cl) - 1]
    mi = cl[0]

    print(ma, mi)
    # 解释器再执行代码时，发现return后有多个值，那么就会将这多个值，直接组包成一个元组
    # 然后将这个元组返回
    return ma, mi

ret = get_max_min()
# ret = ma, mi -> ret = (ma, mi)
print(ret)
print(type(ret))