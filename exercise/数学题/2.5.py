# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 2.5.py
# Time       ：2021/7/16 10:22
# Author     ：zyz
# version    ：python 3.7
"""

"""
计算求1+2-3+4-5... ...100 的值
"""
sum = 0
for i in range(2, 101):
    if i % 2 == 0:
        sum += i
    else:
        sum -= i
sum = sum + 1
print(sum)
