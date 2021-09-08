# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 5.3.py
# Time       ：2021/7/27 13:42
# Author     ：zyz
# version    ：python 3.7
"""

"""
在以下文本中找出 每行中长度超过3的单词:
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick
"""
a = """Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick"""
print([[j for j in i.split(" ") if len(j) > 3] for i in a.split("\n")])
