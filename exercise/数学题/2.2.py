# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 2.2.py
# Time       ：2021/7/16 10:22
# Author     ：zyz
# version    ：python 3.7
"""

"""
如果一个正整数等于除它本身之外其他所有除数之和，就称之为完全数。
例如：6是完全数，因为6 = 1+2+3；
下一个完全数是28 = 14+7+4+2+1。
求1000以下的完全数
"""

for i in range(1, 1000):
    sum = 0
    for j in range(1, i + 1):
        if i % j == 0:
            sum += j
    if 2 * i == sum:
        print(i)
