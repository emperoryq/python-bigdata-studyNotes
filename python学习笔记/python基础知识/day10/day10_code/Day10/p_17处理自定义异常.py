from p_16自定义异常 import *


try:
   num =  get_phone_number()
except (PhoneNumberLengthError, PhoneNumberNotDigitError) as e:
    print(e)
else:
    print(num)
