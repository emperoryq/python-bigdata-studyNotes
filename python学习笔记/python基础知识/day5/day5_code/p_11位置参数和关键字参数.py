'''
位置参数和关键字参数
'''

# 位置参数
def show(n, s):
    for c in s:
        print(f'{n} -- {c}')

# show(1, 'hello')

# show('hello', 1)

# show(1) # TypeError: show() missing 1 required positional argument: 's'

# 关键字参数
# 关键字参数解决了参数在传递时的顺序问题，可以无序传递

show(s = 'hello', n = 1)

show(n = 1, s = 'world')