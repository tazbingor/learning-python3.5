#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/23 下午12:11
# @Author  : Aries
# @Site    : 
# @File    : py008_number.py
# @Software: PyCharm
# 数字

# 加减乘除
print(1 + 2)
print(3 - 2)
print(8 * 8)
print(8 / 1)  # 默认返回浮点数

# str()
age = 24
# message = "Happy " + age + "rd Birthday!"
# TypeError: Can't convert 'int' object to str implicitly
# python无法像java和c#一样自动转字符串
message = "Happy " + str(age) + "rd Birthday!"
print(message)

# 2-8 数字 8:编写 4 个表达式,它们分别使用加法、减法、乘法和除法运算,但结 果都是数字 8。
print(1 + 1)
print(16 - 8)
print(2 * 4)
print(16 / 2)

# 2-9 最喜欢的数字:将你最喜欢的数字存储在一个变量中,
# 再使用这个变量创建一条消息,指出你最喜欢的数字,然后将这条消息打印出来。
num = 65
print("CS ID:" + str(num))
