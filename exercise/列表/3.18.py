# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.18.py
# Time       ：2021/7/16 15:21
# Author     ：zyz
# version    ：python 3.7
"""

"""
过滤掉列表中不及格的学生
a = [
{"name": "张三", "score": 66},
{"name": "李四", "score": 88},
{"name": "王五", "score": 90},
{"name": "陈六", "score": 56},
]
"""
a = [
    {"name": "张三", "score": 66},
    {"name": "李四", "score": 88},
    {"name": "王五", "score": 90},
    {"name": "陈六", "score": 56},
]

f = filter(lambda x: x.get("score") > 60, a)

print(list(f))
