# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test16.py
# Time       ：2021/9/8 9:02
# Author     ：zyz
# version    ：python 3.7
"""


class Test(object):
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        print('这个是类装饰器')
        self.__func(*args, **kwargs)


@Test
def log1():
    print("你好")
