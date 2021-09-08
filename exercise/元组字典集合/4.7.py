# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 4.7.py
# Time       ：2021/7/23 16:57
# Author     ：zyz
# version    ：python 3.7
"""

"""
map函数对列表a=[1,3,5],b=[2,4,6]相乘得到[2,12,30]
"""

a = [1, 3, 5]
b = [2, 4, 6]
print(list(map(lambda x, y: x * y, a, b)))
