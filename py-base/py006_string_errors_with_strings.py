#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-10-22 上午6:20
# @Author  : Aries
# @Site    : 
# @File    : py006_string_errors_with_strings.py
# @Software: PyCharm

# python 字符串中常见的错误操作
# 正确的使用单引号和双引号
# 正确写法
message = "One of Python's strengths is its diverse community."
print(message + "\n")
# 错误写法
# message = 'One of Python's strengths is its diverse community.'
# print(message) # SyntaxError: invalid syntax

#如何在字符串中表示单引号和双引号？
print("余则成说：\"把茶叶交给可浓同志.!\"")
print("余则成强调道：\'一定要把把茶叶交给可浓同志.!\'")