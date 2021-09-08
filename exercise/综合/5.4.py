# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 5.4.py
# Time       ：2021/7/27 13:48
# Author     ：zyz
# version    ：python 3.7
"""

"""
有一个数据list of dict如下
a = [
{"yoyo1": "123456"},
{"yoyo2": "123456"},
{"yoyo3": "123456"},
]
写入到本地一个txt文件，内容格式如下：
yoyo1,123456
yoyo2,123456
yoyo3,123456
"""
a = [
    {"yoyo1": "123456"},
    {"yoyo2": "123456"},
    {"yoyo3": "123456"},
]

with open('../../5.4.txt', 'w', encoding='utf-8') as f:
    for i in a:
        for k, v in i.items():
            f.writelines('{},{}'.format(k, v))
            f.writelines('\r')
    f.close()
