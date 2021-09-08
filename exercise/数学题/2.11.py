# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 2.11.py
# Time       ：2021/7/16 10:22
# Author     ：zyz
# version    ：python 3.7
"""

"""
已知一个数列：1、1、2、3、5、8、13、。。。。的规律为从 3 开始的每一项都等于其前两项的和，这是斐波那契数列。
求满足规律的 100 以内的所有数据
"""


def fun(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fun(n - 2) + fun(n - 1)


print(fun(100))
