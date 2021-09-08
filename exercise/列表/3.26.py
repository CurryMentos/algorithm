# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.26.py
# Time       ：2021/7/22 9:33
# Author     ：zyz
# version    ：python 3.7
"""

"""
L = [1, 2, 3, 5, 6]，如何得出 '12356'？
"""
L = [1, 2, 3, 5, 6]
print(''.join([str(i) for i in L]))
