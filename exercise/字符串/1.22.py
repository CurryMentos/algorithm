# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.22.py
# Time       ：2021/7/15 13:31
# Author     ：zyz
# version    ：python 3.7
"""

"""
s = "ajldjlajfdljfddd"，去重保留原来的顺序，输出"adfjl"
"""


def fun():
    s = "ajldjlajfdljfddd"
    l = list(set(s))
    str_s = ''
    print(str_s.join(l))


fun()
