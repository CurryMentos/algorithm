# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 4.9.py
# Time       ：2021/7/23 17:14
# Author     ：zyz
# version    ：python 3.7
"""

"""
reduce函数计算1！+2！+3！+。。。+10！
"""

from functools import reduce

li = []
for i in range(1, 10):
    li.append(reduce(lambda x, y: x * y, range(1, i + 1)))
print(li)
sum = reduce(lambda x, y: x + y, li)
print(sum)
