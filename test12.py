# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test10.py
# Time       ：2021/6/17 9:55
# Author     ：zyz
# version    ：python 3.7
"""


def file():
    with open('RawFile.txt', 'r+', encoding='utf-8') as f:
        f.write(f.read().replace('&', '\n'))
        f.close()


if __name__ == '__main__':
    file()
