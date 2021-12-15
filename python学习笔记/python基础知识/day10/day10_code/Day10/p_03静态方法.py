'''
静态方法
'''

# 设计 一个编码工具类
class EncodeUtil(object):

    n = 1

    # 编码方法
    @staticmethod
    def encode_data(data, format):
        print(f'对数据 {data} 使用 {format} 格式 进行了编码')


    # 解码方法
    @staticmethod
    def decode_data(data, format):
        print(EncodeUtil.n)
        print(f'对数据 {data} 使用 {format} 格式 进行了解编码')



# 测试
# eu = EncodeUtil()
# eu.encode_data('hello','utf-8')


EncodeUtil.encode_data('Hello','utf-8')
EncodeUtil.decode_data("hello",'GBK')