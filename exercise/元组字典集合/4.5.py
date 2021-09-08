# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 4.5.py
# Time       ：2021/7/23 16:48
# Author     ：zyz
# version    ：python 3.7
"""

"""
map函数,有个列表a = [1, 2, 3, 4] 计算列表中每个数除以2 取出余数 得到 [1,0,1,0]
"""
a = [1, 2, 3, 4]
print(list(map(lambda x: x % 2, a)))
