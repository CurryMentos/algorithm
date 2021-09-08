# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 2.9.py
# Time       ：2021/7/16 10:22
# Author     ：zyz
# version    ：python 3.7
"""

"""
求1+2!+3!+...+10!的和
"""
num = 1
sum = 0
for i in range(1, 11):
    num *= i
    sum += num
print(sum)
