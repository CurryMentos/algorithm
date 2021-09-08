# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test9.py
# Time       ：2021/6/16 15:22
# Author     ：zyz
# version    ：python 3.7
"""
# 猜数字小游戏
import random

l = list(random.sample(range(10), 4))
# print(l)  # 打印数组
count = 0  # 猜测次数
max_count = 8  # 最大猜测次数，可修改以增加或降低难度

while count < max_count:
    print("请输入你猜的四位数字")
    num = list(input())
    A_num = 0  # 数字和位置均正确数
    B_num = 0  # 数字正确位置错误数
    for i in range(len(num)):
        if len(list(set(num))) < len(num):
            print("输入数字重复")
            break
        elif len(num) != len(l):
            print("输入位数不正确")
            break
        elif num[0:len(num)] == str(l[0:len(l)]):
            break
        elif num[i] in str(l):
            if num[i] == str(l[i]):
                A_num += 1
            else:
                B_num += 1
    if A_num == 4 and B_num == 0:
        print("恭喜你猜对啦！")
        break
    else:
        count += 1
        print("{}A{}B".format(A_num, B_num))
        print("当前尝试第{}次".format(count))
    if count == max_count:
        print("游戏结束")
        print("正确答案：{}".format(l))
        break
