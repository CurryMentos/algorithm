# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.16.py
# Time       ：2021/7/16 15:01
# Author     ：zyz
# version    ：python 3.7
"""

"""
a = ["张三","张四","张五","王二"] 如何删除姓张的
"""
a = ["张三", "张四", "张五", "王二"]
for i in a[::-1]:
    if i[0] == "张":
        a.remove(i)
print(a)
