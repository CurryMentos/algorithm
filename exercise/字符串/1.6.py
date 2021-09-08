# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.6.py
# Time       ：2021/7/14 16:16
# Author     ：zyz
# version    ：python 3.7
"""

"""
打印99乘法表
"""


def fun():
    for i in range(10):
        print()
        # 正序
        for j in range(1, i + 1):
        # 逆序
        # for j in range(i, 10):
            print(str(i) + "x" + str(j) + "=" + str(i * j), '\t', end="")


fun()
