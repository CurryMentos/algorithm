# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.11.py
# Time       ：2021/7/15 11:53
# Author     ：zyz
# version    ：python 3.7
"""

"""
输出指定字符串A在字符串B中第一次出现的位置,如果B中不包含A,则输出-1
从 0 开始计数
A = "hello"
B = "hi how are you hello world, hello yoyo !"
"""
import re


def fun():
    A = "hello"
    B = "hi how are you hello world, hello yoyo !"
    if re.findall(A, B):
        print(re.search(A, B).span()[0])
    else:
        print(-1)


fun()
