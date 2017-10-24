#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/24 上午10:06
# @Author  : Aries
# @Site    : 
# @File    : py012_list_sort.py
# @Software: PyCharm
# list 排序


# 正向排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
print(cars)

# 临时排序
print(sorted(cars))
print(cars)

# 反向排序
cars.sort(reverse=True)
print(cars)

# 反向打印列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# 列表长度
print(len(cars))
