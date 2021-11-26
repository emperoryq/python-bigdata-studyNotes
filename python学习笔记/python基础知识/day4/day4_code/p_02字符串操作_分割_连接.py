'''
b. 分割_连接
		split()	掌握  输出的是列表,需要注意有分隔符,且每个都会生效
		splitlines() 理解  注意只识别换行为分隔符

		partition()	 了解  只会分割成三部分,且输出一个元组
		rpartition() 了解
		join() 掌握  加入字符进行连接列表中的每个元素
'''

s = 'Hello World Hello World Hello Python'

# split() 分割函数
def test_split():
    ret = s.split(' ')
    print(ret)
    print(type(ret))

    ret = s.split('o')
    print(ret)

    ret = s.split('ll')
    print(ret)

    # 参数一是要分割的条件字符串
    # 参数二是最大分割次数
    ret = s.split('ll', 1)
    print(ret)

    ss = 'Hello\tWorld Hello\nWorld Hello Python'
    print(ss)
    # 如果在分割字符串时，需要使用任何空白进行分割，那么参数中，什么也不需要写
    ret = ss.split()
    print(ret)

# test_split()


# splitlines() 按行分割
def test_splitlines():
    ss = 'Hello\tWorld Hello\nWorld Hello Python'
    print(ss.splitlines())

    print(ss.split('\n'))

# test_splitlines()

# partition 分割
# 按分割条件将字符串分割成三部分，分割条件前，分割条件，分割条件后
def test_partition():
    ss = 'HellohahaHelloHellohahaHello'
    print(ss.partition('haha'))

    # rpartition() 从右侧进行分割
    ss = 'HellohahaHelloHellohahaHello'
    print(ss.rpartition('haha'))

# test_partition()

# join() 使用当前字符串连接参数中的每个元素
def test_join():
    ss = 'Hello World Python'
    print('-'.join(ss))

    # join 的作用
    s_ss = ss.split()
    print(s_ss)
    # j_ss = '$'.join(s_ss)
    j_ss = '_'.join(s_ss)
    print(j_ss)

    print('$'.join('AB'))

test_join()