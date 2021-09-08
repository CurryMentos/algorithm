# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 4.6.py
# Time       ：2021/7/23 16:54
# Author     ：zyz
# version    ：python 3.7
"""

"""
map函数将列表 [1,2,3,4,5] 使用python方法转变成 [1,4,9,16,25]
"""


def fun(x):
    return x ** 2


print(list(map(fun, [1, 2, 3, 4, 5])))
