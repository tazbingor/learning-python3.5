#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-10-22 上午6:40
# @Author  : Aries
# @Site    : 
# @File    : py007_string_exercise.py
# @Software: PyCharm
# 字符串练习

# 2-3 个性化消息:将用户的姓名存到一个变量中,并向该用户显示一条消息。
username = "余则成"
print("%s斩钉截铁的说道:\"我是深海！\"" % username)  # 使用字符串占位符 %s

# 2-4 调整名字的大小写:将一个人名存储到一个变量中,再以小写、大写和首字母
# 大写的方式显示这个人名。
username = "Nicholas c.zakas"
print(username.upper())  # NICHOLAS C.ZAKAS
print(username.lower())  # nicholas c.zakas
print(username.title())  # Nicholas C.Zakas

# 2-5 名言:找一句你钦佩的名人说的名言,将这个名人的姓名和他的名言打印出来。(包括引号)
print("Benjamin Disraeli : \"A country does not have permanent friends，only permanent interests\"")

# 2-6 名言 2:重复练习 2-5,但将名人的姓名存储在变量 famous_person 中,再创建
# 要显示的消息,并将其存储在变量 message 中,然后打印这条消息。
famous_person = "Benjamin Disraeli"
message = "\"A country does not have permanent friends，only permanent interests.\""
print(famous_person.strip() + " : " + message.strip())

# 2-7 剔除人名中的空白:存储一个人名,并在其开头和末尾都包含一些空白字符。
# 务必至少使用字符组合 "\t" 和 "\n" 各一次。
# 打印这个人名,以显示其开头和末尾的空白。然后,分别使用剔除函数 lstrip() 、
# rstrip() 和 strip() 对人名进行处理,并将结果打印出来。
username = "\t余则成\t"
print(username + "\n")
print(username.lstrip() + "\n")
print(username.rstrip() + "\n")
print(username.strip() + "\n")
