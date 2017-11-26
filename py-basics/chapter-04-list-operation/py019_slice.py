#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/25 下午5:31
# @Author  : Aries
# @Site    : 
# @File    : py019_slice.py
# @Software: PyCharm
# 切片

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# 若没有索引,则从头开始切片
print(players[:2])

# 反之亦然
# 从列表下标为2的元素开始切片
print(players[2:])

# 负数也可以
print(players[-3:])
print("\n")

# 遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli', 'eminem']
print("Here are the first three players on my team:")
for player in players[:4]:
    print(player.title())
print("\n")
# 复制列表
new_players = players  # 此处的赋值并非复制了列表,它们仍在使用同一块列表
new_players.append('nas')
print(new_players)
print(players)  # 结果一致
print("\n")

# 所以
next_players = players[:]
players.remove('eminem')
print(players)
print(next_players)
