# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.15.py
# Time       ：2021/7/16 14:44
# Author     ：zyz
# version    ：python 3.7
"""

"""
统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
"""
a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
print("该列表中有{}个正数{}个负数".format(len([i for i in a if i > 0]), len([j for j in a if j < 0])))
