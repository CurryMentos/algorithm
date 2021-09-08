# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.14.py
# Time       ：2021/7/16 14:44
# Author     ：zyz
# version    ：python 3.7
"""

"""
使用列表推导式，将列表中a = [1, 3, -3, 4, -2, 8, -7, 6]
找出大于0的数，重新生成一个新的列表
"""
a = [1, 3, -3, 4, -2, 8, -7, 6]
print([i for i in a if i > 0])
