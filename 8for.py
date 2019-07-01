#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# forin 循环
# 主要用于把 list 或 tuple 中的每个元素迭代出来
forin_list = ['one', 'two', 'three', 'four', 'five']
forin_list_result = ''
for number_string in forin_list:
    forin_list_result += number_string
print('forin_list_result计算结果为：', forin_list_result)

# forin 计算累加之后
# 注意：Python 提供一个 range() 函数，可以生成一个整数序列（0-∞）,
# range() 函数只是生成一个整数序列，还需要使用 list() 函数，把整数序列转换为 list
forin_range_result = 0
for number_range in list(range(101)):
    forin_range_result += number_range
print('forin_range_result的结果为：', forin_range_result)

# while 循环
# 只要条件满足，就不断循环，条件不满足时退出循环
while_sun = 0
while_n = 0
while while_n < 100:
    while_sun += while_n
    while_n = while_n + 1
print('while_sun的计算结果为：', while_sun)

# while 循环（只计算 0-100 之内奇数和）
while_odd_sun = 0
while_odd_n = 1
while while_odd_n < 100:
    while_odd_sun += while_odd_n
    while_odd_n = while_odd_n + 2
print('0-100 以内奇数和为：', while_odd_sun)

# while 循环（只计算 0-100 之内偶数和）
while_even_sun = 0
while_even_n = 0
while while_even_n < 100:
    while_even_sun += while_even_n
    while_even_n = while_even_n + 2
print('0-100 以内偶数和为：', while_even_sun)

# break 退出循环
# break 语句可以在循环过程中直接退出循环，
# 大多数循环并不需要用到 break 语句
while_break_sun = 0
while_break_n = 0
while while_break_n < 100:
    while_break_sun += while_break_n
    while_break_n = while_break_n + 1
    if while_break_n == 3:
        print('while 循环中退出循环时，while_break_n 的值为：', while_break_n)
        break
    print('while 循环中 while_break_n 的值为：', while_break_n, while_break_sun)
print('while_break_sun 的计算结果为：', while_break_sun)

# continue 跳过某些循环
# continue 语句可以提前结束本轮循环，并直接开始下一轮循环，
# 大多数循环并不需要用到 continue 语句
while_continue_sun = 0
while_continue_n = 0
while while_continue_n < 100:
    while_continue_n = while_continue_n + 1
    if while_continue_n % 2 == 0:
        print('while 循环中跳过的值为：', while_continue_n)
        continue
    while_continue_sun += while_continue_n
    print('while 循环中 while_continue_n 的值为：', while_continue_n, while_continue_sun)
print('while_continue_sun 的计算结果为：', while_continue_sun)
