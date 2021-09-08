# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.21.py
# Time       ：2021/7/15 13:31
# Author     ：zyz
# version    ：python 3.7
"""

"""
s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
"""


def fun():
    s = "ajldjlajfdljfddd"
    l = list(set(s))
    str_s = ''
    for i in range(len(l) - 1):
        flag = True
        for j in range(len(l) - i - 1):
            if ord(l[j]) > ord(l[j + 1]):
                l[j], l[j + 1] = l[j + 1], l[j]
                flag = False
    print(str_s.join(l))


fun()
