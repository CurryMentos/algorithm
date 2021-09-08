# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 2.10.py
# Time       ：2021/7/16 10:22
# Author     ：zyz
# version    ：python 3.7
"""

"""
求s=a+aa+aaa+aaaa+aa...a的值
如：n = 5  a = 3
33333 = 3x10**4+ 3x10**3+ 3x10**2 + 3x10**1 +3x10**0
"""


def fun(n, a):
    sum = 0
    for i in range(n):
        sum += a * 10 ** i
    print(sum)


fun(5, 3)
