# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test7.py
# Time       ：2021/6/15 11:06
# Author     ：zyz
# version    ：python 3.7
"""


def multi():
    for i in range(1, 10):
        print()
        # 正序
        # for j in range(1, i + 1):
        # 逆序
        for j in range(i, 10):
            print(str(i) + "x" + str(j) + "=" + str(i * j), '\t', end="")


if __name__ == '__main__':
    multi()
