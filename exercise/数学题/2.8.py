# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 2.8.py
# Time       ：2021/7/16 10:22
# Author     ：zyz
# version    ：python 3.7
"""

"""
阶乘的意思: 10!=10x9x8x7x6x5x4x3x2x1
求10!
"""
num = 1
for i in range(1, 11):
    num *= i
print(num)
