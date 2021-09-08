# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 5.5.py
# Time       ：2021/7/27 14:17
# Author     ：zyz
# version    ：python 3.7
"""

"""
写一个小程序：控制台输入邮箱地址（格式为 username@companyname.com）， 程序识别用户名和公司名后，将用户名和公司名输出到控制台。
要求：

校验输入内容是否符合规范（xx@yy.com）, 如是进入下一步，如否则抛出提 示"incorrect email format"。注意必须以.com 结尾
可以循环“输入--输出判断结果”这整个过程
按字母 Q（不区分大小写）退出循环，结束程序
"""
import re

while True:
    email = input()
    if email == "q" or email == "Q":
        quit()
    if re.match(r'^[0-9a-zA-Z]{0,19}@[0-9a-zA-Z]{0,19}\.com$', email):
        userName = re.findall("^(.*?)@", email)
        print(userName[0])
        companyName = re.findall("@(.*?).com", email)
        print(companyName[0])
    else:
        print("incorrect email format")
