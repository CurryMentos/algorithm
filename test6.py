# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test6.py
# Time       ：2021/6/11 10:11
# Author     ：zyz
# version    ：python 3.7
"""


class Emp(object):
    def __init__(self, name, age, job, salary):
        self.name = name
        self.age = age
        self.job = job
        self.salary = salary

    def show(self):
        print(self.name, self.age, self.job, self.salary)


class Worker(Emp):
    def __init__(self, name, age, job, salary, bonus, address, email):
        super().__init__(name, age, job, salary)
        self.bonus = bonus
        self.address = address
        self.email = email

    def show(self):
        print(self.name, self.age, self.job, self.salary)

    def showAll(self):
        print(self.name, self.age, self.job, self.salary, self.bonus, self.address, self.email)


if __name__ == '__main__':
    w = Worker("阿祖", 27, "测试", "20k", "2k", "上海", "123@qq.com")
    w.show()
    w.showAll()
