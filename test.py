# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test.py
# Time       ：2021/6/2 16:13
# Author     ：zyz
# version    ：python 3.7
"""


class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


print(Solution().climbStairs(17))
