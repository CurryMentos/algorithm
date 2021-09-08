# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.15.py
# Time       ：2021/7/15 11:53
# Author     ：zyz
# version    ：python 3.7
"""

"""
如何判断一个字符串是不是纯数字组成
a = "123456"
b = "yoyo123"
"""

a = "123456"
b = "yoyo123"


def fun(n):
    try:
        int(n)
    except Exception:
        print("该字符串不由纯数字组成")
    else:
        print("该字符串由纯数字组成")


fun(a)
fun(b)
