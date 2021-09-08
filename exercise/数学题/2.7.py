# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 2.7.py
# Time       ：2021/7/16 10:22
# Author     ：zyz
# version    ：python 3.7
"""

"""
计算公式 13 + 23 + 33 + 43 + …….+ n3
实现要求：
输入 : n = 5
输出 : 165
对应的公式 : 13 + 23 + 33 + 43 + 53 = 225
"""


def fun():
    n = 5
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 3
    print(sum)


fun()
