# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.21.py
# Time       ：2021/7/16 15:21
# Author     ：zyz
# version    ：python 3.7
"""

"""
a = [
'my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I',
'need', 'skills', 'more', 'my', 'ability', 'are',
'so', 'poor'
]
统计列表中每个成员出现的次数
"""
a = [
    'my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I',
    'need', 'skills', 'more', 'my', 'ability', 'are',
    'so', 'poor'
]
from collections import Counter

l1 = list(dict(Counter(a)).keys())
l2 = list(dict(Counter(a)).values())
for i in range(len(l1)):
    print("元素{}出现{}次".format(l1[i], l2[i]))
