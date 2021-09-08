# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test10.py
# Time       ：2021/6/17 9:55
# Author     ：zyz
# version    ：python 3.7
"""

import random, string, re


def mobile():
    mobile_pre = ['131', '186', '158']
    mobile_next = ''.join(random.sample(string.digits, 8))
    mobile = random.choice(mobile_pre) + mobile_next
    return mobile


def pwd():
    pwd = ''.join(random.sample(string.digits + string.ascii_letters, random.randint(8, 20)))
    pattern_num = r"\d"
    pattern_lower = "[a-z]"
    pattern_upper = "[A-Z]"
    patter_num_continue = ".*?(123456789)"
    flag = False
    while flag is False:
        try:
            re.search(pattern_num, pwd).group()
            re.search(pattern_lower, pwd).group()
            re.search(pattern_upper, pwd).group()
        except Exception:
            return "密码不包含数字或大小写字母"
        else:
            if re.match(patter_num_continue, pwd):
                return "密码出现连续数字"
            else:
                flag = True
    return pwd


def create_file():
    with open('login.csv', 'w', encoding='utf-8') as f:
        f.writelines('mobile,pwd')
        for i in range(10):
            f.writelines('\r')
            f.writelines('{},{}'.format(mobile(), pwd()))
        f.close()


if __name__ == '__main__':
    print(pwd())
    # create_file()
