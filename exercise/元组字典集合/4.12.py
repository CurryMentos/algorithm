# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 4.12.py
# Time       ：2021/7/27 11:25
# Author     ：zyz
# version    ：python 3.7
"""

"""
d={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
字典根据键从小到大排序
"""
d = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}
print(dict(sorted(d.items())))
