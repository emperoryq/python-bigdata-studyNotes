'''
混合参数的写法
'''

def func(a,b,c,d,e, *args,f=1,g=2,**kwargs):
    print(a, b, c, d, e)
    print(args)
    print(f, g)
    print(kwargs)

func(1, 2, 3 ,4, 5)
func(1, 2, 3 ,4, 5, 5, 6, 7, 8, 9)
func(1, 2, 3 ,4, 5, 5, 6, 7, 8, 9, f = 10, g = 11)
func(1, 2, 3 ,4, 5, 5, 6, 7, 8, 9, f = 10, g = 11, h = 333, i = 444)