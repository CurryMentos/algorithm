# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.28.py
# Time       ：2021/7/23 14:17
# Author     ：zyz
# version    ：python 3.7
"""

"""
如下列表
people = [
{"name":"yoyo", "age": 20},
{"name":"admin", "age": 28},
{"name":"zhangsan", "age": 25},
]
按年龄age从小到大排序
"""
people = [
    {"name": "yoyo", "age": 20},
    {"name": "admin", "age": 28},
    {"name": "zhangsan", "age": 25},
]

for i in range(len(people) - 1):
    if people[i].get("age") > people[i + 1].get("age"):
        people[i], people[i + 1] = people[i + 1], people[i]
print(people)
