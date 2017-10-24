#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/24 上午10:50
# @Author  : Aries
# @Site    : 
# @File    : py014_working_with_lists.py
# @Software: PyCharm
# 操作列表

# 遍历集合
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 注意缩进,错误的缩进会影响整个循环的结果
# PS:缩进,相当于java或C中的大括号,相当于一个简写的代码块儿
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")
