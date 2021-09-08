# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.23.py
# Time       ：2021/7/15 13:31
# Author     ：zyz
# version    ：python 3.7
"""

"""
画菱形
"""


def fun():
    for i in [3, 2, 1, 0, 1, 2, 3]:
        print(i * " " + (7 - 2 * i) * "*" + i * " ", '\t')


fun()
