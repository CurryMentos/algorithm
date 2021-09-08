# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.9.py
# Time       ：2021/7/14 16:37
# Author     ：zyz
# version    ：python 3.7
"""

"""
题目:输入一个字符串str, 输出第m个只出现过n次的字符，如在字符串 gbgkkdehh 中,
找出第2个只出现1 次的字符，输出结果：d
"""
from collections import Counter


def fun():
    str = "gbgkkdehh"
    print(Counter(str))
    m = 2  # 出现个数
    n = 1  # 出现次数
    l1 = list(Counter(str).keys())
    l2 = list(Counter(str).values())
    if m not in range(len(l1)):
        print("所输入超出字符出现次数上限")
    elif n > max(l2):
        print("所输入超出单个字符个数上限")
    else:
        for i in l2[::-1]:
            if i == n:
                pass
            else:
                l1.pop(l2.index(i))
                l2.remove(i)
        print("第{}个出现{}次的字符是{}".format(m, n, l1[m - 1]))
    # l = [i for i, j in dict(Counter(str)).items() if j == n]
    # print(l[m-1])


fun()
