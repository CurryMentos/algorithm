# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 2.1.py
# Time       ：2021/7/16 10:22
# Author     ：zyz
# version    ：python 3.7
"""

"""
如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
那么问题来了，求1000以内的水仙花数（3位数）
"""
for i in range(100, 1000):
    a = i % 10
    b = int(i / 100)
    c = int((i - b * 100) / 10)
    if i == a ** 3 + b ** 3 + c ** 3:
        print(i)
