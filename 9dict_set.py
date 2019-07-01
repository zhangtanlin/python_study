#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dict 字典（类似json格式）
# 在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
dict_name_age = {'zhao': 20, 'qian': 50, 'sun': 19, 'li': 99}
print('dict_name_age中zhao的年龄为：', dict_name_age['zhao'])

# 设置字典
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
dict_name_class = {'zhao': '一年级', 'qian': '二年级', 'sun': '三年级', 'li': '四年级'}
dict_name_class['qian'] = '六年级'
print(
    '设置dict_name_class中qian的年级为：',
    dict_name_class['qian'],
    '。dict_name_class全部值为：',
    dict_name_class
)

# dict中如果 key 不存在，dic 就会报错
# 要避免 key 不存在的错误，有两种办法：
# 一是：通过 in 判断 key 是否存在,
# 二是：通过dict提供的get() 方法，如果 key 不存在，可以返回 None ，或者自己指定的 value,
# dict.get('xx') 如果 xx 在 dict 里面返回 xx 的值，否则返回 None，
# dict.get('xx', 'aaaa') 如果 'xx' 这个 key 不在 dict 里面，就把 'aaaa' 赋值给 'xx'，
# 返回None的时候Python的交互环境不显示结果。
dict_name_company = {'zhao': 'X公司', 'qian': 'Y公司', 'sun': 'Z公司'}
if 'li' in dict_name_company:
    print('li在dict_name_company字典中')
else:
    print('li没有在dict_name_company字典中')

if dict_name_company.get('zhou', 'A公司'):
    print('zhou在dict_name_company字典中')
else:
    print('zhou没有在dict_name_company字典中')

# 字典中要删除一个 key ，用 pop(key) 方法，对应的 value 也会从 dict 中删除
# dict 内部存放的顺序和 key 放入的顺序是没有关系的；
# 和 list 比较，dict 有以下几个特点：
# 查找和插入的速度极快，不会随着 key 的增加而变慢，
# 需要占用大量的内存，内存浪费多；
# 而 list 相反：
# 查找和插入的时间随着元素的增加而增加，
# 占用空间小，浪费内存很少。
# 注意： dict 可以用在需要高速查找的很多地方，在 Python 代码中几乎无处不在，
# 正确使用 dict 非常重要，需要牢记的第一条就是 dict 的 key 必须是不可变对象。
# 这是因为 dict 根据key来计算 value 的存储位置，如果每次计算相同的 key 得出的结果不同，那 dict 内部就完全混乱了。
# 这个通过 key 计算位置的算法称为哈希算法（ Hash ）。
# 要保证 hash 的正确性，作为 key 的对象就不能变。
# 在 Python 中，字符串、整数等都是不可变的，因此，可以放心地作为 key 。
# 而 list 是可变的，就不能作为 key ：
dict_pop_name = {'feng': 1, 'chen': 2, 'chu': 3, 'wei': 4}
dict_pop_name.pop('chu')
print('在dict_pop_name字典中，删除chu为：', dict_pop_name)

# set
# set 和 dict 类似，也是一组 key 的集合，但不存储 value 。由于 key 不能重复，所以，在 set 中，没有重复的 key。
# 注意： set 获取的的是没有 value 的 json 对象，
# 创建 set ，需要提供一个 list 作为输入集合，
# 重复元素在 set 中自动被过滤，
name_set = set([1, 2, 3, 4])
print('name_set的值为：', name_set)

# 通过 add(key) 的方式可以往 set 中添加元素
age_set = set([1, 2, 3, 4, 5])
age_set.add(999)
print('age_set 添加 key 后的值为：', age_set)

# 通过 romove(key) 可以删除元素
# 注意：删除元素后元素顺序可能会变，但是这也说明 set 里面的元素的无序性
class_set = set(['一年级', '二年级', '三年级', '四年级', '五年级', '六年级'])
class_set.remove('一年级')
print('class_set 删除一个元素后的值为：', class_set)

# set 可以看成数学意义上的无序和无重复元素的集合，所以两个 set 可以做数学意义上的交集并集等操作
company_set1 = set([1, 2, 3])
company_set2 = set([2, 3, 4])
print('company_set1 和 company_set2 的交集是：', company_set1 & company_set2)
print('company_set1 和 company_set2 的并集是：', company_set1 | company_set2)

# set 和 dict 的原理一样，所以不可以放入可变对象（ set 里面的元素不能为可变的值），
# 例如： set 里面不能含有 list 类型的值；但是可以为 tuple ，因为元组的值不可修改。
# 因为无法判断两个可变对象是否相等，也就无法保证 set 内部不会有重复元素。
# 注意：如果set里面含有 tuple ，此时元组里面的不能含有 list 元素，原理同上。
# set_list = set(['1','2','3',['4-1','4-2','4-3'],'5']) # 会报错
set_tuple = set(['1','2','3',('4-1','4-2','4-3'),'5'])
# set_tuple_list = set(['1','2','3',('4-1','4-2',[22,23,24,25]),'5']) # 会报错
print('set_tuple 的值为：', set_tuple)

# 比较可变对象和不可变对象
# 对于可变对象，比如 list ，进行操作， list 里面的内容是会变化的。
# 对于不变对象来说，调用对象（比如： changeable_str 自己）自身的任意方法，
# 也不会改变该对象自身的内容（比如： changeable_str 的值 abcdafg ）；
# 相反，这些方法会创建新的对象（比如： new_changeable_str 和 XYZbcdXYZfg ）并返回，
# 这样，就保证了不可变对象本身永远是不可变的。
changeable_list = ['a','c','b']
changeable_str = 'abcdafg'
print('changeable_list 进行排序后的值是：', changeable_list.sort())
new_changeable_str = changeable_str.replace('a', 'XYZ')
print('changeable_str 把a替换为XYZ后为：', new_changeable_str)
