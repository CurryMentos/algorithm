# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test13.py
# Time       ：2021/6/22 10:09
# Author     ：zyz
# version    ：python 3.7
"""


class A():
    def __init__(self):
        self.__Gender()
        self.Name()

    def __Gender(self):
        print("A.__Gender")

    def Name(self):
        print("A.Name")


class B(A):
    def __Gender(self):
        print("B.__Gender")

    def Name(self):
        print("B.Name")


b = B()
