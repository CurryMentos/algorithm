# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test5.py
# Time       ：2021/6/9 11:09
# Author     ：zyz
# version    ：python 3.7
"""
for x in range(0, 101):
    for y in range(0, 101 - x):
        if 15 * x + 9 * y + (100 - x - y) == 300:
            print('公鸡：{},母鸡：{},小鸡：{}'.format(x, y, 100 - x - y))
