'''
函数中存在多个return语句
'''

def get_num():
    return 1
    return 2
    return 3

print(get_num()) # 1
