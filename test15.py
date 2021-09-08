# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test15.py
# Time       ：2021/7/15 9:25
# Author     ：zyz
# version    ：python 3.7
"""
import string

str = "a1b23c456d7890"
l = []
for i in str:
    try:
        int(str[i])
        str.replace(str[i], " ")
        l.append(i)
    except Exception:
        pass
print(str)
print(l[::-1])
