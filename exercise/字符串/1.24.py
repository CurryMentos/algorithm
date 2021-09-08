# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.24.py
# Time       ：2021/7/15 13:31
# Author     ：zyz
# version    ：python 3.7
"""

"""
题目 给一个不多于5位的正整数，要求：
一、求它是几位数，
二、逆序打印出各位数字。
a = 12345
"""


def fun():
    a = 92743
    num = a // 10
    if num < 1:
        print("1位数")
        print(a)
    elif 1 <= num < 10:
        print("2位数")
        print(10 * (a % 10) + a // 10)
    elif 10 <= num < 100:
        print("3位数")
        print(100 * (a % 10) + 10 * (a // 10 % 10) + a // 100)
    elif 100 <= num < 1000:
        print("4位数")
        print(1000 * (a % 10) + 100 * (a // 10 % 10) + 10 * (a // 100 % 10) + a // 1000)
    elif 1000 <= num < 10000:
        print("5位数")
        print(10000 * (a % 10) + 1000 * (a // 10 % 10) + 100 * (a // 100 % 10) + 10 * (a // 1000 % 10) + a // 10000)


fun()
