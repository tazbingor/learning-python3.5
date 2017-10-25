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
