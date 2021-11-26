'''
函数的默认值参数
'''

def show(a = 0, b = 0):
    print(f'a:{a}, b:{b}')
    print(a + b)

show() # 0 + 0
show(1) # 1 + 0
show(1, 2) # 1 + 2

# 使用默认值参数时 ，需要注意：
# 在默认值参数的右侧，不能再出现没有默认值参数

def display(a, b = 0, c = 0):
    print(a, b, c)

# display(1)
# display(1, 2)
# display(1, 2, 3) SyntaxError: non-default argument follows default argument
