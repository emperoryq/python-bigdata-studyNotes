'''自定义异常

格式 ：
class 异常名Error(Exception):
    pass
'''

# 定义一个用来判断当前手机号是否有非法字符的异常
class PhoneNumberNotDigitError(Exception):
    pass


# 定义一个用来判断手机号位数是否合法的异常
class PhoneNumberLengthError(Exception):
    def __init__(self,msg):
        self.__msg = msg


    def __str__(self):
        return self.__msg



# 定义一个函数，用来获取一个电话号码
def get_phone_number():
    pn = input('请输入一个11位的手机号：')
    if pn.isdigit() == False:
        # 抛出自定义的异常
        raise PhoneNumberNotDigitError()
    elif len(pn) != 11:
        raise PhoneNumberLengthError('手机号位数不正确')

    return '输入的手机号是合法的：' + pn













