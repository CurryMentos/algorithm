# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.14.py
# Time       ：2021/7/15 11:53
# Author     ：zyz
# version    ：python 3.7
"""

"""
输入一个姓名，判断是否姓王
a = "王五"
b = "老王"
"""

a = "王五"
b = "老王"


def fun(n):
    if isinstance(n, str):
        if len(n) > 0:
            if n[0] == "王":
                print("此人姓王")
            else:
                print("此人不姓王")


fun(a)
fun(b)
