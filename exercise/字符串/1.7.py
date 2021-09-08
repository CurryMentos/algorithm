# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.7.py
# Time       ：2021/7/14 16:20
# Author     ：zyz
# version    ：python 3.7
"""

"""
找出单词 "welcome" 在 字符串"Hello, welcome to my world." 中出现的位置，找不到返回-1
从下标0开始索引
"""
import re


def fun():
    str = "Hello, welcome to my world."
    if re.findall("welcome", str):
        print(re.search("welcome", str).span())
    else:
        print(-1)


fun()
