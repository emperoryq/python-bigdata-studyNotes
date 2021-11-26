'''
字符串的定义
'''

s1 = 'hello'
s2 = "hello"
s3 = '''hello'''
s4 = """hello"""

print(s1 * 3)
print(s2 * 3)
print(s3 * 3)
print(s4 * 3)


# 使用下标访问字符串中的字符

s = 'hello'
print(s[0])
print(s[2])
# print(s[5]) # IndexError: string index out of range

print('hello'[0])