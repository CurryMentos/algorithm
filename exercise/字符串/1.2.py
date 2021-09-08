# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.2.py
# Time       ：2021/7/14 15:03
# Author     ：zyz
# version    ：python 3.7
"""

"""
回文的定义："回文" 就是正读倒读都一样的。
如奇数个："98789"，这个数字正读是"98789" 倒读也是"98789"。
偶数个数字"3223"也是回文数。
字母 "abcba" 也是回文。
判断一个字符串是否是回文字符串，是打印True， 不是打印False
"""


def fun():
    l1 = list(input())
    l2 = l1[::-1]
    if l1 == l2:
        print(True)
    else:
        print(False)


fun()
