#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 切片 slice(index,index_length)
# 取一个 list 或 tuple 的前 N 个元素（也就是索引为 0-(N-1) 的元素），
# 利用 python 的切片（ Slice ）操作符，能大大简化这种操作。
# 例如： [0:3] 表示，从索引 0 开始取，直到索引 3 为止，但不包括索引 3 。即索引 0,1,2 正好是 3 个元素。
number_slice = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
print('number_slice 使用 slice获取 0-3 元素为', number_slice[0: 2])
print('number_slice 使用 slice获取 1-3 元素为', number_slice[1: 3])
print('number_slice 使用 slice获取 1-4 元素为', number_slice[1: 4])
