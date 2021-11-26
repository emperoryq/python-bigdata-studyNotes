'''
set-list-tuple三者类型间转换
'''

s = 'hello'
print(s)

l = list(s)
print(l)

print(set(l))

print(set(s))

ll = str(l) # __str__
print(ll, type(str(l)))
print(''.join(l))

print(tuple(s))