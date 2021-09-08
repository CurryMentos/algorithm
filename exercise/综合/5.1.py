# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 5.1.py
# Time       ：2021/7/27 11:36
# Author     ：zyz
# version    ：python 3.7
"""

"""
有1、2、3、4数字能组成多少互不相同无重复数的三位数?
分别打印这些三位数的组合
"""
from itertools import permutations

a = [1, 2, 3, 4]
# for i in a:
#     for j in a:
#         for k in a:
#             if i != j and i != k and j != k:
#                 print(i, j, k)
for i, j, k in permutations(a, 3):
    print(i, j, k)
