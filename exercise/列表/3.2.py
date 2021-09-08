# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.2.py
# Time       ：2021/7/16 11:51
# Author     ：zyz
# version    ：python 3.7
"""

"""
如果有一个列表a=[1,3,5,7,11]
问题：1如何让它反转成[11,7,5,3,1]
2.取到奇数位值的数字，如[1,5,11]
"""
a = [1, 3, 5, 7, 11]
print(a[::-1])
print(a[::2])
