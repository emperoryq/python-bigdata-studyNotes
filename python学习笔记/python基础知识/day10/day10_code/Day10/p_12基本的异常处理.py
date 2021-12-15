'''
使用 try-except 进行基本的异常处理

'''

s = 'Hello'

try:
    # 这句代码会发生异常
    print(s.index('O'))
# except ValueError:
except Exception:
    print('查找的子串不存在')

# 使用Try 来尝试执行 后面语句 块中的代码 ，如果代码 发生异常问题
# 那么异常信息就会被 except 捕捉到，可以在 except 后面进行异常处理
# 如果代码 没有异常，那么程序就正常运行，不会执行except 后的代码


print('over')