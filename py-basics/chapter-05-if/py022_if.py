#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/27 上午10:13
# @Author  : Aries
# @Site    : 
# @File    : py22_if.py
# @Software: PyCharm
# if语句

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
