'''
字符串遍历
'''

def test_chars(s):
    # 方式一
    for c in s:
        print(c)

    # 方式二
    for i in range(len(s)):
        print(i, '-', s[i])

    # 方式三
    i = 0
    while i < len(s):
        print(s[i])
        i += 1

test_chars('hello')