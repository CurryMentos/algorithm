# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test2.py
# Time       ：2021/6/7 10:06
# Author     ：zyz
# version    ：python 3.7
"""


def sum(a, b):
    c = 0
    if a == b:
        print("两数相等")
    elif a > b:
        for i in range(b, a):
            if i % 2 == 0:
                c += i
    elif a < b:
        for i in range(a, b):
            if i % 2 == 0:
                c += i
    print(c)


sum(17, 17)
