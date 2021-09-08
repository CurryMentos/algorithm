# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test17.py
# Time       ：2021/9/8 13:19
# Author     ：zyz
# version    ：python 3.7
"""

text = "http协议监测模型-今日新增数据断言%xpath%//*[@id='mainContent']/div/div/div[1]/div[2]/div%0%0&实体网络检测行为模型"
a = []
b = []
s = 0
for line in text:
    s = s + 1
    a = text.split("&")
print(a)
for i in a:
    print(i)
    name, em1, em1v, num1, num2 = i.split("%")
    print(name)
    print(em1)
    print(em1v)
    print(num1)
    print(num2)
    # b = [name, em1, em1v, num1, num2]
    # print(b)
