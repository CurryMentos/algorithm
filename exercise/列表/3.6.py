# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.6.py
# Time       ：2021/7/16 11:51
# Author     ：zyz
# version    ：python 3.7
"""

"""
取出列表中最大的三个值
L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
"""
L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
print(sorted(L1)[len(L1) - 3:len(L1)])
