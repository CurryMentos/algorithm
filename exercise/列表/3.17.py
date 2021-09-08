# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.17.py
# Time       ：2021/7/16 15:21
# Author     ：zyz
# version    ：python 3.7
"""

"""
题1：有个列表a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8] 使用filter 函数过滤出大于0的数
题2：列表b = ["张三", "张四", "张五", "王二"] 过滤掉姓张的姓名
"""
a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
b = ["张三", "张四", "张五", "王二"]

f1 = filter(lambda x: x > 0, a)
f2 = filter(lambda x: x[0] != "张", b)

print(list(f1))
print(list(f2))
