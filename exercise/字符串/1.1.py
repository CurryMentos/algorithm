# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.1.py
# Time       ：2021/7/14 14:38
# Author     ：zyz
# version    ：python 3.7
"""

"""
已知 a的值为"hello"，b的值为"world"，如何交换a和b的值？
得到a的值为"world"，b的值为"hello"
"""


def fun():
    a = "hello"
    b = "world"
    a, b = b, a
    print(a)
    print(b)


fun()
