# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 4.10.py
# Time       ：2021/7/23 17:34
# Author     ：zyz
# version    ：python 3.7
"""

"""
两个字典合并a={"A":1,"B":2},b={"C":3,"D":4}
"""
a = {"A": 1, "B": 2}
b = {"C": 3, "D": 4}
a.update(b)
print(a)
