# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.5.py
# Time       ：2021/7/14 16:15
# Author     ：zyz
# version    ：python 3.7
"""

"""
把字符串 s 中的每个空格替换成"%20"
输入：s = "We are happy."
输出："We%20are%20happy."
"""


def fun():
    s = "We are happy."
    print(s.replace(" ", "%20"))


fun()
