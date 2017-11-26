#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/25 下午5:49
# @Author  : Aries
# @Site    : 
# @File    : py020_slice_exercise.py
# @Software: PyCharm
# 切片练习

# 4-10 切片:选择你在本章编写的一个程序,在末尾添加几行代码,以完成如下任务。
# 打印消息“The first three items in the list are:”,再使用切片来打印列表的前三个元素。
# 打印消息“Three items from the middle of the list are:”,再使用切片来打印列表中间的三个元素。
# 打印消息“The last three items in the list are:”,再使用切片来打印列表末尾的三个元素。
cakes = ['摊煎饼', '烙饼', '炒饼', '千层饼', '老婆饼', '油饼']
print("The first three items in the list are:")
print(cakes[:3])
print("The first three items in the list are:")
print(cakes[3:])
print("The last three items in the list are:")
print(cakes[-3:])

# 4-11 你的比萨和我的比萨:在你为完成练习 4-1 而编写的程序中,创建比萨列表的
# 副本,并将其存储到变量 friend_pizzas 中,再完成如下任务。
# 在原来的比萨列表中添加一种比萨。
# 在列表 friend_pizzas 中添加另一种比萨。
# 核实你有两个不同的列表。为此,打印消息“My favorite pizzas are:”,
# 再使用一个 for 循环来打印第一个列表;
# 打印消息“My friend’s favorite pizzas are:”,
# 再使用一个 for 循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。
pizzas = ['大葱肉末披萨', '宫保鸡丁披萨', '韭菜鸡蛋披萨']
friend_pizzas = pizzas[:]
friend_pizzas.append('芝士土豆披萨')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend’s favorite pizzas are:")

for friend_pizza in friend_pizzas:
    print(friend_pizza)
print('\n')
# 4-12 使用多个循环:在本节中,为节省篇幅,程序 foods.py 的每个版本都没有使用 for 循环来打印列表。
# 请选择一个版本的 foods.py,在其中编写两个 for 循环,将各个食品列表都打印出来。
my_foods = ['pizza', 'falafel', 'carrot cake']
print("我爱吃:")
for my_food in my_foods:
    print(my_food)

foods = my_foods[:]
foods.append('ice cream')
print("我依然爱吃:")

for food in foods:
    print(food)
