# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 5.2.py
# Time       ：2021/7/27 13:28
# Author     ：zyz
# version    ：python 3.7
"""

"""
a = [11, 2, 33, 1, 5, 88, 3]
冒泡排序
"""
a = [11, 2, 33, 1, 5, 88, 3]
for i in range(len(a) - 1):
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)
