# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.23.py
# Time       ：2021/7/16 17:16
# Author     ：zyz
# version    ：python 3.7
"""

"""
给定一个整数数组nums 和一个目标值target ，请你在该数组中找出和为目标值的那两个整数，并返回他
们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:
给定nums=[2，7，11，15]，target=9
因为nums[0] + nums[1] =2+7 = 9
所以返回[0， 1]
"""


def fun():
    nums = [2, 7, 11, 15]
    target = 18
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print([i, j])


fun()
