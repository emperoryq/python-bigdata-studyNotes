'''
if 的使用格式
'''
#if
# def is_net(age):
#     if age >= 18:
#         print('可以上网')
#
# age = int(input('请输入你的年龄：'))
# is_net(age)

#if-else
# def is_net(age):
#     if age >= 18:
#         print('可以上网')
#     else:
#         print('年龄不够，不准上网，滚去学习')
#
# age = int(input('请输入你的年龄：'))
# is_net(age)

'''
练习：
定义一个函数
接收一个数字参数，判断该数字是否是偶数
'''

# 定义一个函数，判断是否是偶数
# def is_even(n):
#     if n % 2 == 0:
#         print(f'{n}是偶数')
#         print('%d是偶数'%n)
#         print('{}是偶数'.format(n))
#     else:
#         print(f'{n}是奇数')
#
# m = int(input('please input number:'))
# is_even(m)

# if-elif-else
# def is_week_day(day):
#     if day == '1' or day == '一':
#         print('星期一')
#     elif day == '2' or day == '二':
#         print('星期二')
#     elif day == '3' or day == '三':
#         print('星期三')
#     elif day == '4' or day == '四':
#         print('星期四')
#     elif day == '5' or day == '五':
#         print('星期五')
#     elif day == '6' or day == '六':
#         print('星期六')
#     elif day == '7' or day == '七':
#         print('星期七')
#     else:
#         print('输错了')
#
# d = input('请输入星期几:')
# is_week_day(d)

# if 语句的嵌套的作用
def is_score_level(score):
    if score >= 0 and score <= 100:

        if score >= 90:
            print('得分%s，级别优'%score)
        elif score >= 80:
            print('得分%s，级别良'%score)
        elif score >= 70:
            print('得分%s，级别中'%score)
        elif score >= 60:
            print('得分%s，级别差'%score)
        else:
            print('得分%s，不及格'%score)
    else:
        print(f'输入成绩{score}无效')

s = int(input('请输入分数：'))
is_score_level(s)



