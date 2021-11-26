'''
元组的遍历
'''

# for-in
t = (1, 2, 3, 4, 5, 'hello')
for v in t:
    print(v)

# 循环配合下标 方式一
for i in range(len(t)):
    print(t[i])

# 循环配合下标 方式二
i = 0
while i < len(t):
    print(t[i])
    i += 1