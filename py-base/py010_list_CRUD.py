#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/24 上午1:53
# @Author  : Aries
# @Site    : 
# @File    : py010_list_CRUD.py
# @Software: PyCharm
# 增删改查

# 修改
tools = ['Java', 'Golang', 'PHP']
print(tools)
tools[2] = 'Python'
print(tools)

# 增加
tools.append('Ruby')  # 在末尾添加元素
print(tools)

# 插入
tools.insert(0, 'C')  # 选择在0下标插入元素
tools.insert(1, 'C++')  # 选择在1下表插入元素
print(tools)

# 删除
# del tools[5]  # 删除下标为5的元素
# print(tools)
# pop()
# popped_tools = tools.pop()  # pop(默认)同时删除并保存list中末尾元素,也可指定删除
# print(tools)
# print(popped_tools)

# 根据值删除元素
tools.remove('Ruby')
print(tools)
