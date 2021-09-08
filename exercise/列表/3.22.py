# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.22.py
# Time       ：2021/7/16 15:21
# Author     ：zyz
# version    ：python 3.7
"""

"""
给定一个整数数组A及它的大小n，同时给定要查找的元素val，
请返回它在数组中的位置(从0开始)，若不存在该元素，返回-1。
若该元素出现多次请返回第一个找到的位置
如 A1=[1, "aa", 2, "bb", "val", 33]
或 A2 = [1, "aa", 2, "bb"]
"""
A1 = ["val", 1, "aa", 2, "bb", "val", 33, "val"]
A2 = [1, "aa", 2, "bb"]


def fun(A, val):
    if val in A:
        print(A.index(val))
    else:
        print(-1)


fun(A1, "val")
fun(A2, "val")
