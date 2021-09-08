# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 4.1.py
# Time       ：2021/7/23 16:29
# Author     ：zyz
# version    ：python 3.7
"""

"""
输出1-100除3余1 的数，结果为tuple
"""
t = (i for i in range(101) if i % 3 == 1)
print(tuple(t))
