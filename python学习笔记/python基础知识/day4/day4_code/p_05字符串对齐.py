'''
e. 对齐 （理解）
		center()	按给定宽度居中显示
		rjust()		右对齐
		ljust()		左对齐
'''

s = 'Hello'
print('|' + s.center(11) + '|')
print('|' + s.center(11, '_') + '|')

print('|' + s.rjust(11) + '|')
print('|' + s.rjust(11, '_') + '|')

print('|' + s.ljust(11) + '|')
print('|' + s.ljust(11, '_') + '|')