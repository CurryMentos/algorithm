# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test3.py
# Time       ：2021/6/7 11:43
# Author     ：zyz
# version    ：python 3.7
"""


def test():
    a = 0
    i = 1
    while i < 101:
        if i % 3 == 0 and i % 5 == 0:
            print(i)
            a += 1
        if a == 4:
            break
        i += 1


test()
