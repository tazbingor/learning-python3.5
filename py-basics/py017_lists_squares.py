#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/25 下午4:20
# @Author  : Aries
# @Site    : 
# @File    : py017_lists_squares.py.py
# @Software: PyCharm
# 使用range()创建数字列表


# 将前10个整数的平方加入到一个列表中
square_list = []

for value in range(1, 11, 1):
    square_list.append(value ** 2)

print(square_list)

# 对数字列表执行简单的统计计算s
print(sum(square_list))  # 总和
print(min(square_list))  # 最小值
print(max(square_list))  # 最大值

# 上述情况的另一种简写
squares = [value ** 2 for value in range(1, 11)]
print(squares)
