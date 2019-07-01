#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 条件判断if elif else
# 注意一：不要少写了冒号（:）
# 注意二：if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，
# 把该判断对应的语句执行后，就忽略掉剩下的elif和else

# 条件判断一（if条件）：
age1 = 20
if age1 > 18:
    print('条件判断一：年龄超过18岁')
else:
    print('未超过18岁')

# 条件判断二（else条件）：
age2 = 16
if age2 > 18:
    print('年龄超过18岁')
else:
    print('条件判断二：未超过18岁')

# 条件判断三（elif条件）：
age3 = 18
if age3 > 18:
    print('年龄超过18岁')
elif age3 == 18:
    print('条件判断三：刚刚18岁')
else:
    print('未超过18岁')

# 判断条件简写
# 只要simple_if是非零数值、非空字符串、非空list等，就判断为True，否则为False
simple_if = True
if simple_if:
    print('简写条件判定成功')

# 条件判定和input()方法的结合
# 注意：input()方法返回的数据类型是str，所以不能直接和数值类型的数据进行交互（会报错）,
# 需要把input()的返回值设置为数值，使用ini()方法。
input_str = int(input())
if input_str < 1000:
    print('input_str小于1000')
elif input_str == 1000:
    print('input_str等于1000')
else:
    print('input_str大于1000')