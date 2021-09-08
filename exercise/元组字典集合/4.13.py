# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 4.13.py
# Time       ：2021/7/27 11:29
# Author     ：zyz
# version    ：python 3.7
"""

"""
a = [2, 3, 8, 4, 9, 5, 6]
b = [2, 5, 6, 10, 17, 11]
1.找出a和b中都包含了的元素
2.a或b中包含的所有元素
3.a中包含而集合b中不包含的元素
"""
a = [2, 3, 8, 4, 9, 5, 6]
b = [2, 5, 6, 10, 17, 11]

print([i for i in a if i in b])
print(list(set([i for i in a + b])))
print([i for i in a if i not in b])
