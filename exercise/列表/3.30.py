# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.30.py
# Time       ：2021/7/23 16:25
# Author     ：zyz
# version    ：python 3.7
"""

"""
有个列表a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
如何打乱列表a的顺序,每次得到一个无序列表
"""

import random

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(a)
print(a)
