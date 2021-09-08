# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 4.4.py
# Time       ：2021/7/23 16:38
# Author     ：zyz
# version    ：python 3.7
"""

"""
a = [1,2,3] 和 b = [(1),(2),(3) ] 以及 c = [(1,),(2,),(3,) ] 的区别？
"""

a = [1, 2, 3]
b = [(1), (2), (3)]
c = [(1,), (2,), (3,)]


def fun(n):
    for i in n:
        print("元素{}的类型为{}".format(i, type(i)))


fun(a)
fun(b)
fun(c)
