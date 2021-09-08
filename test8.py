# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test8.py
# Time       ：2021/6/15 16:16
# Author     ：zyz
# version    ：python 3.7
"""
import re

with open('response.txt', 'rb') as f:
    reg = re.compile(r'"comboId": (\d{6})')
    print(reg.findall(str(f.read())))
