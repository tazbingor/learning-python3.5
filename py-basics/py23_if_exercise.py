#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/27 上午10:22
# @Author  : Aries
# @Site    : 
# @File    : py23_if_exercise.py
# @Software: PyCharm
# if 练习

# 5-1 条件测试:编写一系列条件测试;将每个测试以及你对其结果的预测和实际结 果都打印出来。
number1 = 10
number2 = 20
print(number1 > number2)  # False
print(number1 < number2)  # True
print(number1 == number2)  # False
print(number1 == 10)  # True
print(number1 == '10')  # False

string1 = '10'
print(string1 == '10')  # True
print(string1 != 10)  # True


def functuon_01():
    return 10


def function_02():
    return 10


print(functuon_01() == function_02())  # True
print("\n")

array1 = []
array2 = []
print(array1 == array2)  # True
print("\n")

tuple = ()
print(array1 == tuple)  # False
print(tuple == ())  # True
print("\n")

print(() == ())  # True
print([] == [])  # True
print(type(array1) == type(array2))  # True
print("\n")
# 由此可知,py中的==和!=只是在比较值



