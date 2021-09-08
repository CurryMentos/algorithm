# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.8.py
# Time       ：2021/7/14 16:37
# Author     ：zyz
# version    ：python 3.7
"""

"""
统计字符串“Hello, welcome to my world.” 中字母w出现的次数
统计单词 my 出现的次数
"""

import re


def fun():
    str = "Hello, welcome to my world."
    print(len(re.findall("w", str)))
    print(len(re.findall("my", str)))


fun()
