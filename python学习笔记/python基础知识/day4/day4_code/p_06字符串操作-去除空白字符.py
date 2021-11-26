'''
	f. 去除空白（理解）
		strip()		去除两端空白
		lstrip()	去除左侧空白
		rstrip()	去除右侧空白
'''

s = '     Hello    world      '
print(s)

print('|' + s.strip() + '|')
print('|' + s.rstrip() + '|')
print('|' + s.lstrip() + '|')

ret = s.split()
ret = ''.join(ret)
print(ret.center(20))