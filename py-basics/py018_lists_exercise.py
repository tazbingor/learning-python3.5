#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/25 下午4:35
# @Author  : Aries
# @Site    : 
# @File    : py018_lists_exercise.py
# @Software: PyCharm
# range练习

import time
import datetime

# 4-3 数到 20:使用一个 for 循环打印数字 1~20(含)。
print([value for value in range(1, 21, 1)])

# 4-4 一百万:创建一个列表,其中包含数字 1~1 000 000,再使用一个 for 循环将这 些数字打印出来
# print([value for value in range(1, 1000001, 1)])

# 4-5 计算 1~1 000 000 的总和:
# 创建一个列表,其中包含数字 1~1 000 000,
# 再使用 min()和 max()核实该列表确实是从 1 开始,到 1 000 000 结束的。
# 另外,对这个列表调 用函数 sum(),看看 Python 将一百万个数字相加需要多长时间。
high_capacity = [value for value in range(1, 1000001, 1)]
print(min(high_capacity))
print(max(high_capacity))

start = time.time()
print(sum(high_capacity))
end = time.time()
print(end - start)  # 0.009526968002319336

# 4-6 奇数:通过给函数 range()指定第三个参数来创建一个列表,其中包含 1~20 的 奇数;
# 再使用一个 for 循环将这些数字都打印出来。
cardinal_number = [value for value in range(1, 20, 2)]
for value in cardinal_number:
    print(value)

# 4-7 3 的倍数:创建一个列表,其中包含 3~30 内能被 3 整除的数字;
# 再使用一个 for 循环将这个列表中的数字都打印出来。
cardinal_numbers = list(range(3, 30, 3))
# print(cardinal_numbers)
for value in cardinal_numbers:
    print(value)

# 4-8 立方:将同一个数字乘三次称为立方。
# 例如,在 Python中,2 的立方用 2**3 表示。
# 请创建一个列表,其中包含前 10 个整数(即 1~10)的立方,再使用一个 for 循 环将这些立方数都打印出来。
squares = [value ** 3 for value in range(1, 11, 1)]
for number in squares:
    print(number)

# 4-9 立方解析:使用列表解析生成一个列表,其中包含前 10 个整数的立方。
squares = [value ** 3 for value in range(1, 11, 1)]
