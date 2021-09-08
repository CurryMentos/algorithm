# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.13.py
# Time       ：2021/7/15 11:53
# Author     ：zyz
# version    ：python 3.7
"""

"""
给定一个数a，判断一个数字是否为奇数或偶数
a1 = 13
a2 = 10
"""

a1 = 13
a2 = 10


def fun(n):
    if n % 2 == 0:
        print("该数为偶数")
    else:
        print("该数为奇数")


fun(a1)
fun(a2)
