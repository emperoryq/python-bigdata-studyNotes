'''
实参和形参
'''

# 定义一个函数

def say_hi(name): # 形参
    print('Hello ', name)
    #print('Hello %s' %name )
    #print(f'Hello {name}')

# say_hi('tom') # 实参
# say_hi('jack')
# say_hi('rose')

def my_sum(a, b):
    print(a + b)

my_sum(1, 2)