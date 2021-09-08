# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.7.py
# Time       ：2021/7/16 11:51
# Author     ：zyz
# version    ：python 3.7
"""

"""
a = [1, -6, 2, -5, 9, 4, 20, -3] 按列表中的数字绝对值从小到大排序
"""
a = [1, -6, 2, -5, 9, 4, 20, -3]
for i in range(len(a) - 1):
    for j in range(len(a) - i - 1):
        if abs(a[j]) > abs(a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)
