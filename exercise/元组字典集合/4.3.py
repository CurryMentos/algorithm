# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 4.3.py
# Time       ：2021/7/23 16:33
# Author     ：zyz
# version    ：python 3.7
"""

"""
将('a', 'b', 'c', 'd', 'e') 和 (1,2, 3, 4, 5)两个tuple转成
（1， 2， 3， 4， 5）为key, ('a', 'b', 'c', 'd', 'e') 为value的字典
"""
t1 = ('a', 'b', 'c', 'd', 'e')
t2 = (1, 2, 3, 4, 5)
print({t2: t1})
