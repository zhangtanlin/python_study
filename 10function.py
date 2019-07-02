#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数
# Python内置了很多有用的函数，我们可以直接调用。
# 注意：调用函数的时候，如果传入的参数数量不对，会报TypeError的错误；
# 如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误。
# https://docs.python.org/3/library/functions.html 含有内置函数名字。
# 调用函数需要根据函数定义，传入正确的参数。如果函数调用出错，一定要学会看错误信息，所以英文很重要！

# 求绝对值的函数
import math
from function_import import my_abs_import
number_abs = abs(-3.1415927)
print('number_abs 的绝对值是：', number_abs)

# 求最大值的函数
number_max = max(82, 3, 7, 11, 5, 4, 23, 100, -100, 6, 8, 5)
print('number_max 最大值是：', number_max)

# python 内置的函数，还包括数据类型转换的函数。
# 注意：字符串样式的 float ，不能转换为 ini , 但是 float 和 int 可互转。
str_float = float('3.1415927')
str_int = int('1415927')
float_int = int(3.1415927)
int_float = float(3)
print('str_float 的数据类型是：', type(str_float), '值是：', str_float)
print('str_ini 的数据类型是：', type(str_int), '值是：', str_int)
print('float_int 的数据类型是：', type(float_int), '值是：', float_int)
print('int_float 的数据类型是：', type(int_float), '值是：', int_float)

# 理解函数
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”。
understandFunction = abs  # 变量 understandFunction 指向 abs 函数
understandFunction(-1)  # 所以也可以通过 understandFunction 调用 abs 函数

# 定义函数
# 定义函数使用（ def 函数名 左括号 参数 有括号 ） 语句。
# 注意：函数内部语句一旦执行到return，函数就完毕，并将结果返回，因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑；
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return；
# 在Python命令行模式下定义函数时，Python会出现...的提示。函数定义结束后需要按两次回车重新回到>>>提示符下。


def my_abs(num):
    if num >= 0:
        return num
    else:
        return -num


use_my_abs = my_abs(-918)
print('use_my_abs 调用函数 my_abs 后为：', use_my_abs)

# 函数的导入
# 千万注意： xxx.py 文件名最好是不要含有数组（严格按照 python 的命名规范进行命名）。
print('导入含有函数的文件，调用my_abs_import方法后结果为：', my_abs_import(-3.14))

# 空函数
# 定义空函数可以使用 pass 作为占位符，比如还没有想好怎么写函数的代码。先放一个 pass 让代码能运行起来。
# 注意：pass是语句什么都不做的， 。


def none_function():
    pass


# pass 作为占位符还可以使用在条件语句里面
name = 'zhangxiaolin'
if name == 'zhangxiaolin':
    pass

# 自定义函数引用时，参数个数不对，Python 解释器会抛出 TypeError ，但是参数类型不对，解释器无法帮我们检查，
# 所以需要在定义参数时对参数类型进行检查


def my_abs_add_type_inspect(num):
    if not isinstance(num, (int, float)):
        raise TypeError('参数类型错误')
    if num >= 0:
        return num
    else:
        return -num
# use_my_abs_type = my_abs_add_type_inspect('985') #这里参数类型是错误的应该报“参数类型错误”
# print('use_my_abs_type 调用参数类型检查函数 my_abs_add_type_inspect 结果为为：', use_my_abs_type)


# 函数怎么返回多个值
# 例如：从已知点（ x , y ）向 angle 度方向移动 step 的距离。
# 注意：从返回值可以看出，返回的是一个 tuple ，
# 在语法上元组可以省略小括号，而多个变量，可以同时接受一个元组，按位置个对应的值，
# 所以Python的函数返回多值，其实返回的就是一个 tuple ，但写起来更方便。


def move(x, y, step, angle=0):
    new_x = x + step * math.cos(angle)
    new_y = y - step * math.sin(angle)
    return new_x, new_y


new_long_let = move(1, 30, 100, 30)
# 值为： (16.425144988758404, 128.8031624092862)
print('从（ 1, 30 ）向 30 度方向移动 100后为：', new_long_let)

# 实验，利用函数写一个一元二次方程的两个解，
# ax²+bx+c=0 求 x 的值。
# 注意：返回值一定不要加小括号，元组默认不需要加小括号的


def solve_equation_one_two(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('a 参数类型错误')
    if not isinstance(b, (int, float)):
        raise TypeError('b 参数类型错误')
    if not isinstance(c, (int, float)):
        raise TypeError('c 参数类型错误')
    pow_b_two = int(math.pow(b, 2))  # b 平方
    new_sqrt = abs(pow_b_two - 4*a*c)  # 平方根
    new_x1 = (-b + new_sqrt)/(2*a)  # 第一个值
    new_x2 = (-b - new_sqrt)/(2*a)  # 第二个值
    return new_x1, new_x2


equation_one_two = solve_equation_one_two(1, 2, 3)
print('一元二次方程equation_one_two，解为：', equation_one_two)  # 解为： (3.0, -5.0)

# 函数的默认参数
# 自定义一个计算X平方的函数


def my_power(x):
    return x * x

# 函数设置三次方和多次方运算时，
# 注意算法，很重要、相当重要、非常重要


def solve_power_n(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


my_solve_power_n = solve_power_n(5, 3)
print('my_solve_power_n 的三次方的值为', my_solve_power_n)

# 在 Python 的函数中，需要设置默认参数是，可以直接给参数设置默认值
# 注意：这种参数的设置类似给typesecipt函数设置默认值
def solve_power_base(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


my_solve_power_solve_power_base = solve_power_base(5, 4)
print('my_solve_power_solve_power_base 的4次方的值为', my_solve_power_solve_power_base)