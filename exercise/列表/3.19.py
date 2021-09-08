# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.19.py
# Time       ：2021/7/16 15:21
# Author     ：zyz
# version    ：python 3.7
"""

"""
有个列表 a = [1, 2, 3, 11, 2, 5, 88, 3, 2, 5, 33]
找出列表中最大的数，出现的位置，下标从0开始
"""
a = [1, 2, 3, 11, 2, 5, 88, 3, 2, 5, 33]
print("最大的数为{}，出现在列表第{}位".format(max(a), a.index(max(a)) + 1))
