# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.29.py
# Time       ：2021/7/23 15:11
# Author     ：zyz
# version    ：python 3.7
"""

"""
现有 nums=[2, 5, 7] ，如何在该数据最后插入一个数字 9 ，如何在2后面插入数字0
"""
import copy

nums = [2, 5, 7]
nums1 = copy.copy(nums)
nums1.append(9)
nums2 = copy.copy(nums)
nums2.insert(1, 0)
print(nums1)
print(nums2)
