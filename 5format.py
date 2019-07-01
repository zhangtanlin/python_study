#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 格式化替换
print('Hello, %s' % 'world')
print('Hi, %s, you have %d 元欠款.' % ('Michael', 1000000))

#替换%可以使用%%来转译
print('我有 %d %% 喜欢你' %50)

#format()格式化
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))