# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.8.py
# Time       ：2021/7/16 11:51
# Author     ：zyz
# version    ：python 3.7
"""

"""
b = ["hello", "helloworld", "he", "hao", "good"]
按list里面单词长度倒叙
"""
b = ["hello", "helloworld", "he", "hao", "good"]
for i in range(len(b) - 1):
    for j in range(len(b) - i - 1):
        if len(b[j]) < len(b[j + 1]):
            b[j], b[j + 1] = b[j + 1], b[j]
print(b)
