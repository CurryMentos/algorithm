# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.25.py
# Time       ：2021/7/19 13:48
# Author     ：zyz
# version    ：python 3.7
"""

"""
a = [[1,2],[3,4],[5,6]] 如何一句代码得到 [1, 2, 3, 4, 5, 6]
"""

a = [[1, 2], [3, 4], [5, 6]]
print([a[i][j] for i in range(len(a)) for j in range(2)])
