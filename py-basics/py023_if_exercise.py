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


# 5-2 更多的条件测试:
# 检查两个字符串相等和不等。
print("1" == "1")  # True
print('1' == "1")  # True
print('2' == '2')  # True
print("\n")

# 使用函数 lower()的测试。
print("WEB".lower() == "WEB")  # false
print("WEB".lower() == "web")  # True
print("\n")

# 检查两个数字相等、不等、大于、小于、大于等于和小于等于。
print(1 == 2)  # false
print(1 != 2)  # True
print(1 > 2)  # false
print(1 < 2)  # True
print(1 >= 2)  # false
print(1 <= 2)  # True
print("\n")

# 使用关键字 and 和 or 的测试。
number_01 = 1
number_02 = 2
print(number1 == number2 and number1 < number2)  # False
print(number1 != number2 and number1 < number2)  # True
print("\n")

print(number1 == number2 or number1 < number2)  # True
print(number1 == number2 or number1 < number2)  # True
print("\n")

# 测试特定的值是否包含在列表中。
three_body = ['叶文洁', '罗辑', '大史']
print('程欣' in three_body)  # False
print('罗辑' in three_body)  # True

# 测试特定的值是否未包含在列表中。
print('程欣' not in three_body)  # True
print('罗辑' not in three_body)  # False
