#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-10-22 上午6:06
# @Author  : xb
# @Site    : 
# @File    : py005_string_stripping_whitespace.py
# @Software: PyCharm

#rstrip(),确保字符串末尾没有空白
favorite_language = " python高级造人设计 "
print(favorite_language.rstrip())

#lstrip()删除字符串头部空白
print(favorite_language.lstrip())

#strip()同时剔除字符串两端的空白
print(favorite_language.strip())