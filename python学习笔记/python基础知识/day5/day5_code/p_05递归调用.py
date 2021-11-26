'''
函数递归调用
    函数在函数体内，又调用了自己，这种形式就是递归调用
'''

# def func():
#     print('Func Start...')
#     func()
#     print('Func Stop...')
#
# func()

# 求阶乘
# 5！ = 1 * 2 * 3 * 4 * 5

# factorial阶乘
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(3))
# print(factorial(5))

'''
factorial(5) -> 5 * factorial(4) -> return 5 * 24 -> 120
                    -> 4 * factorial(3) -> return 4 * 6
                            -> 3 * factorial(2) -> return 3 * 2
                                    -> 2 * factorial(1) -> return 2 * 1
                                            -> return 1 
'''