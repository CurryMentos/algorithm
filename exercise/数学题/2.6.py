# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 2.6.py
# Time       ：2021/7/16 10:22
# Author     ：zyz
# version    ：python 3.7
"""

"""
定义一个函数：计算 1-n 之间的所有 5 的倍数之和，默认计算 1-100 （ n 是 一个整数）
"""


def fun():
    n = 100
    sum = 0
    for i in range(1, n):
        if i % 5 == 0:
            sum += i
    print(sum)


fun()
