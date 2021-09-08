# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 4.11.py
# Time       ：2021/7/23 17:46
# Author     ：zyz
# version    ：python 3.7
"""

"""
m1={'a':1,'b':2,'c':1} # 将同样的value的key集合在list里，输出{1:['a','c'],2:['b']}
"""

m1 = {'a': 1, 'b': 2, 'c': 1}
l = [(i[1], i[0]) for i in m1.items()]
m2 = {}
for i in l:
    if i[0] in m2.keys():
        m2[i[0]].append(i[1])
    else:
        m2[i[0]] = [i[1]]
print(m2)
