'''
模块查找顺序
'''

import sys
# print(sys.path)

import p_06模块

import os

# import pymysql
sys.path.append('C:\\Users\\KG\\Desktop')

import AAAA
print(AAAA.n)
print(sys.path)