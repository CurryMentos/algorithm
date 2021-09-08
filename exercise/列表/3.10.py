# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.10.py
# Time       ：2021/7/16 13:42
# Author     ：zyz
# version    ：python 3.7
"""

"""
将列表中的重复值取出(仅保留第一个)，要求保留原始列表顺序
如a=[3, 2, 1, 4, 2, 6, 1] 输出[3, 2, 1, 4, 6]
"""
a = [9, 9, 5, 3, 1, 2, 3, 2, 9]
for i in range(len(a)):
    num = a.pop()
    if num not in a:
        a.insert(0, num)
print(a)
