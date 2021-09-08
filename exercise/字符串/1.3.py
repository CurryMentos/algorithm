# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.3.py
# Time       ：2021/7/14 16:07
# Author     ：zyz
# version    ：python 3.7
"""

"""
已知一个字符串为 "hello_world_yoyo", 如何得到一个队列 ["hello","world","yoyo"]
"""


def fun():
    str = "hello_world_yoyo"
    a, b, c = str.split("_")
    l = [a, b, c]
    print(l)


fun()
