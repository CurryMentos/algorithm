# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.20.py
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
找出列表中出现次数最多的元素
"""
a = [
    'my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I',
    'need', 'skills', 'more', 'my', 'ability', 'are',
    'so', 'poor'
]
from collections import Counter

d = dict(Counter(a)).items()
l = [i for i, j in d if j == max(dict(Counter(a)).values())]
print("列表中出现次数最多的元素为{}".format(l))
