'''
列表操作-查找
'''

l = [1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 2, 3]

# count()
print(l.count(6))
print(l.count(66))

# index
print(l.index(6))
print(l.index(2))
# print(l.index(22)) ValueError: 22 is not in list

# in - not in
print(2 in l)
print(22 in l)

print(2 not in l)
print(22 not in l)