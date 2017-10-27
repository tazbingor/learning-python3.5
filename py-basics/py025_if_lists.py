#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/27 上午11:52
# @Author  : Aries
# @Site    : 
# @File    : py25_if_lists.py
# @Software: PyCharm

# 如何判断一个列表是否为空?
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
print('\n')

# 确定多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
