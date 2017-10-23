#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/23 下午12:49
# @Author  : Aries
# @Site    : 
# @File    : py009_list.py
# @Software: PyCharm
#  列表

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)
# print(bicycles[0])

#
# 3-1 姓名:将一些朋友的姓名存储在一个列表中,并将其命名为 names。
# 依次访问 该列表中的每个元素,从而将每个朋友的姓名都打印出来
names = ['奈文摩尔', '斯文', '编织者']
for i in names:
    print(i)

# 3-2 问候语:继续使用练习 3-1 中的列表,但不打印每个朋友的姓名,而为每人打
# 印一条消息。每条消息都包含相同的问候语,但抬头为相应朋友的姓名。
for i in names:
    print(i + "，你惊天吃了么？")

# 3-3 自己的列表:想想你喜欢的通勤方式,如骑摩托车或开汽车,并创建一个包含 多种通勤方式的列表。
# 根据该列表打印一系列有关这些通勤方式的宣言,如“I would like I would like
# to own a Honda motorcycle”。
commutingTools = ['汽车', '飞机', '公路自行车']
for i in commutingTools:
    print(i + "我的最爱！")
