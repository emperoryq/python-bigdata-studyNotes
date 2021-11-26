'''
	a.查找_替换_统计
		find()  掌握		注意: 找不到子串时,返回-1
		rfind() 了解
		index() 了解		注意: 找不到子串时,程序会崩溃,产生一条异常信息,导致程序无法执行
		rindex() 了解
		replace() 掌握   默认全部替换
		count()	掌握
'''

s = 'Hello World Hello World Hello Python'

def test_find():
    # find查找
    idx = s.find('orld') # 默认起始结束位置
    print(idx)

    idx = s.find('orld', 8) # 设置起始位置
    print(idx)

    idx = s.find('orld', 8, 20) # 设置起始位置和结束位置
    print(idx)

test_find()

def test_index():
    idx = s.index('orld')
    print(idx)

    # idx = s.index('orld', 8, 20) # 找不到子串时，程序会崩溃，并产生一条异常信息，导致程序无法执行：ValueError: substring not found
    # print(idx)

test_index()

def test_rfind_rindex():
    print(s.rfind('o'))
    print(s.rindex('o'))

test_rfind_rindex()

# replace() 替换
def test_replace():
    # 替换时默认替换所有的符合的字子串
    idx = s.replace('l', 'L')
    print(idx)
    print(s) # 字符串替换以后，原来字符串不变

    # 最后的参数3表示替换个数
    print(s.replace('l', 'L', 3))

test_replace()

# count 计数统计
def test_count():
    print(s.count('o'))

    print(s.count('o', 1, 5))

test_count()