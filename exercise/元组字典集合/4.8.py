# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 4.8.py
# Time       ：2021/7/23 17:01
# Author     ：zyz
# version    ：python 3.7
"""

"""
reduce函数计算1-100的和
"""
from functools import reduce

sum = reduce(lambda x, y: x + y, [i for i in range(101)])
print(sum)
