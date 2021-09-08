# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.10.py
# Time       ：2021/7/15 11:48
# Author     ：zyz
# version    ：python 3.7
"""

"""
判断字符串a="welcome to my world" 是否包含单词b="world"
包含返回 True，不包含返回 False
"""
import re


def fun():
    a = "welcome to my world"
    b = "world"
    if re.findall(b, a):
        print(True)
    else:
        print(False)


fun()
