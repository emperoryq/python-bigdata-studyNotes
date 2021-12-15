'''
函数sort
'''

my_list = [7,2, 4,1, 5, 8, 9, 3, 0, 6]

my_list.sort()

print(my_list)

my_list = [{'id':1, 'name':'tom', 'age':12},{'id':3, 'name':'rose', 'age':32},{'id':2, 'name':'Jack', 'age':22}]

# 默认sort方法是不能对字典进行比较排序的，TypeError: '<' not supported between instances of 'dict' and 'dict'
# 按id的升序排序.
# my_list.sort(key=lambda d : d['id'])
# 按年龄的降序排序2
my_list.sort(key=lambda d : d['age'], reverse=True)

print(my_list)

list = ['1', '2', '3', '4', '5']
print(list[10:])