# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test13.py
# Time       ：2021/6/22 10:09
# Author     ：zyz
# version    ：python 3.7
"""


def print_list(n: list):
    for i in n:
        if isinstance(i, int):
            print(i)
        else:
            print_list(i)


if __name__ == '__main__':
    alist = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
    print(print_list(alist))
