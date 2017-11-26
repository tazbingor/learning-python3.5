#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/24 上午11:29
# @Author  : Aries
# @Site    : 
# @File    : py016_making_numerical_lists.py
# @Software: PyCharm
# 创建数值列表

# 打印1-5之间的数字
for num in range(1, 6):
    print(num)

print("\n")

# range 指定步长
# 打印1~10内的偶数
even_number = list(range(2, 11, 2))
print(even_number)

