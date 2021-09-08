# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 5.6.py
# Time       ：2021/7/27 15:33
# Author     ：zyz
# version    ：python 3.7
"""

"""
判断一个字符串的括号自否闭合（包括大小中括号）
左括号和右括号必须是一一对应
"""


def fun(str):
    a = []
    flag = True
    for i in str:
        if i == "{" or i == "[" or i == "(":
            a.append(i)
        elif i == "}":
            if len(a) == 0 or a.pop() != "{":
                return False
        elif i == "]":
            if len(a) == 0 or a.pop() != "[":
                return False
        elif i == ")":
            if len(a) == 0 or a.pop() != "(":
                return False
    if len(a) != 0:
        flag = False
    return flag


if __name__ == '__main__':
    str1 = "{[([{}])]}"
    str2 = "{[([{}])][}]"
    print(fun(str1))
    print(fun(str2))
