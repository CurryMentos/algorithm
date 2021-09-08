# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.9.py
# Time       ：2021/7/16 13:37
# Author     ：zyz
# version    ：python 3.7
"""

"""
L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
如何用一行代码得出[1, 2, 3, 5, 11, 33, 88]
L2 = [1, 2, 3, 4, 5] ,L[10:]结果是多少（报错？还是None，还是[]）
"""

L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
L2 = [1, 2, 3, 4, 5]

print(sorted(list(set(L1))))
print(L2[10:])
