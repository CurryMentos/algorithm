# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.27.py
# Time       ：2021/7/22 9:33
# Author     ：zyz
# version    ：python 3.7
"""

"""
a = ["a", "b", "c"]
b = [1, 2, 3]
如何得到 {'a': 1, 'b': 2, 'c': 3}
"""
a = ["a", "b", "c"]
b = [1, 2, 3]
u, v, w = a
x, y, z = b
print({u: x, v: y, w: z})
