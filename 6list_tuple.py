#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list
# list的索引超出范围时，会报IndexError错误，确保索引不越界，
# 记得最后一个元素的索引是len(classmates) - 1
name_list = ['zhang', 'xiao', 'lin']
print('name_list的长度是：', len(name_list))
print('name_list的第1个值是：', name_list[0])
print('name_list的第2个值是：', name_list[1])
print('name_list的最后个值是（写法一）：', name_list[-1])
print('name_list的最后个值是（写法二）：', name_list[len(name_list)-1])
print('name_list的倒数第2个值是：', name_list[-2])

# 添加数据到list末尾
age_list = [10, 11, 12, 13]
age_list.append(15)
print('age_list添加数字15后的值为：', age_list)

# 删除数据list末尾的值
class_list1 = ['一年级', '二年级', '三年级', '四年级', '五年级']
class_list2 = ['一年级', '二年级', '三年级', '四年级', '五年级']
class_list1.pop()
print('class_list1删除末位的值为：', class_list1)
class_list2.pop(2)
print('class_list2删除索引2的值为：', class_list2)

# 替换索引的值，可以直接采用赋值的方式
country_list = ['中国', '美国', '欧罗斯', '法国', '英国']
country_list[3] = '德国'
print('把country_list索引3的值改为德国，country_list为：', country_list)

# list内部的数据类型
list_type = ['我', True, 18]
print('list_type可以包含多种数据类型,list_type为：', list_type)

# list内部可以包含list
child_list1 = ['childFirst1', 'childSecond1', 'childThird1']
parent_list1 = ['first1', 'second1', child_list1, 'third1']
parent_list2 = [
    'first2',
    'second2',
    [
        'childFirst2',
        'childSecond2',
        'childThird2'
    ],
    'third2'
]
print('parent_list1的子列表child_list1，索引为1的值是：', parent_list1[2][1])
print('list内部可以包含list，parent_list2为：', parent_list2)

# 元组（tuple）
# 元组（tuple）list很相似，唯一的区别是，元组（tuple）一旦初始化就不能修改
# 元组没有 append()、insert()等方法，其他获取元素的方法和list一样
name_tuple = ('元组1', '元组2', '元组3', '元组4')
print('元组name_tuple为:', name_tuple)

# 定义一个空元组
# 注意：如果使用tuple = (1)，定义的不是元组，而是定义的数值1，
# 因为()小括号即可以表示tuple还可以表示数据里算公式中的小括号，
# 所以python规定这种情况按小括号进行计算，结果位1
empty_tuple = ()
print('空元组empty_tuple为：', empty_tuple)
tuple_number = (1)
print('tuple_number定义的是一个1，而不是定义了一个元组，tuple_number为：', tuple_number)

# 有且只有一个元素的元素
one_element_tuple = ('Iam is one element tuple.')
print('有且只有一个元素的元组，one_element_tuple为：', one_element_tuple)

# 如果tuple（元组）里面嵌套list（列表），
# 改变list的数据时，元组不算被改变.
# 原因：表面上看tuple的元素变了，但其实变的不是tuple的元素，而是list的元素。
# tuple一开始指向的list并没有改成别的list，
# 所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
# 即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，
# 但指向的这个list本身是可变的！
tuple_list = ('我', '爱', ['中国', '巴基斯坦'], '们')
tuple_list[2][0] = '巴基斯坦'
tuple_list[2][1] = '中国'
print('修改tuple_list（元组）里面list（list）为：', tuple_list)
