# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.1.py
# Time       ：2021/7/16 11:48
# Author     ：zyz
# version    ：python 3.7
"""

"""
如何判断一个数组是对称数组：
要求：判断数组元素是否对称。例如[1，2，0，2，1]，[1，2，3，3，2，1]这样的都是对称数组
用Python代码判断，是对称数组打印True，不是打印False,如：
x = [1, "a", 0, "2", 0, "a", 1]
"""


def fun(n):
    if n == n[::-1]:
        print(True)
    else:
        print(False)


fun([1, 2, 0, 2, 1])
