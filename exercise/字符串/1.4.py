# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.4.py
# Time       ：2021/7/14 16:11
# Author     ：zyz
# version    ：python 3.7
"""

"""
有个列表 ["hello", "world", "yoyo"]如何把把列表里面的字符串联起来，
得到字符串 "hello_world_yoyo"
"""


def fun():
    l = ["hello", "world", "yoyo"]
    a, b, c = l
    str = a + "_" + b + "_" + c
    print(str)


fun()
