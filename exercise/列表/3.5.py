# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.5.py
# Time       ：2021/7/16 11:51
# Author     ：zyz
# version    ：python 3.7
"""

"""
a = ["hello", "world", "yoyo", "congratulations"]
找出列表中单词最长的一个
"""
a = ["hello", "world", "yoyo", "congratulations"]
for i in range(len(a) - 1):
    for j in range(len(a) - i - 1):
        if len(a[j]) > len(a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]
print(a.pop())
