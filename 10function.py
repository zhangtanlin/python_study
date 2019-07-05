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
# 自定义一个计算 x 平方的函数


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
# 这种参数的设置类似给 typesecipt 函数设置默认值
# 注意：必选参数在前，默认参数在后，否则 Python 的解释器会报错；
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。


def solve_power_base(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


my_solve_power_solve_power_base = solve_power_base(5, 4)
print('my_solve_power_solve_power_base 的4次方的值为',
      my_solve_power_solve_power_base)

# 函数中按顺序提供参数和不按顺序提供参数的区别写法


def enroll(name, grade, age=6, city='成都'):
    print('姓名是：', name)
    print('年级是：', grade)
    print('年龄是：', age)
    print('城市是：', city)


enroll('张小', '一年级')  # 使用默认参数，添加姓名、班级
enroll('张小小', '二年级', 10)  # 设置默认参数，添加姓名、班级、年龄
enroll('张小小小', '三年级', city='广元')  # 不按顺序修改默认参数，添加姓名、班级、城市

# 当参数为 list 时，常见问题
# 注意：函数在定义时，默认参数 l 的值就被计算出来了，即 []，
# 因为默认参数 l 也是一个变量，它指向对象 []，
# 每次调用该函数，如果改变了 l 的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的 [] 了。


def param_list(l=[]):
    l.append('结束')
    return l


print('param_list 使用默认参数时：', param_list())  # 结果=> ['结束']
print('param_list 添加参数时：', param_list([1, 2, 3]))  # 结果=> [1, 2, 3, '结束']
print('param_list 再次使用默认参数时：', param_list())  # 结果=> ['结束', '结束']
print('param_list 第三次使用默认参数时：', param_list())  # 结果=> ['结束', '结束', '结束']

# 修改上面的 param_list 为正确方式
# 注意：在下面代码中，为什么设置参数为str、None这样的不变对象呢？
# 因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误；
# 此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读取这条数据一点问题都没有；
# 我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。


def change_param_list(l=None):
    if l is None:
        l = []
    l.append('再次结束')
    return l


print('change_param_list 使用默认参数时：', change_param_list())  # ['再次结束']
print('change_param_list 添加参数时：', change_param_list([1, 2]))  # [1, 2, '再次结束']
print('change_param_list 再次使用默认参数时：', change_param_list())  # ['再次结束']
print('change_param_list 第三次使用默认参数时：', change_param_list())  # ['再次结束']

# 可变参数
# 可变参数就是传入的参数个数是可变的，可以是 1 个、 2 个到任意个，还可以是 0 个。
# 注意这种可变参数一般都会涉及到在函数内部循环；
# variable_list_square_sum 函数只能传入 list ；
# variable_tuple_square_sum 函数只能传入 tuple 元组；
# 可变参数允许你传入 0 个或任意个参数，这些可变参数在函数调用时自动组装为一个 tuple ；


def variable_list_square_sum(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print('variable_list_square_sum 里面 list 的平方和为：',
      variable_list_square_sum([1, 2, 3]))


def variable_tuple_square_sum(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print('variable_tuple_square_sum 里面数据的平方和为：',
      variable_tuple_square_sum(4, 5, 6))

variable_square_sum1 = variable_tuple_square_sum(*(7, 8, 9))
variable_square_sum2 = variable_tuple_square_sum(*[7, 8, 9])

print('把 list 或者 tuple 作为可变参数计算平方和为：',
      variable_square_sum1, variable_square_sum2)

# 关键字参数
# 关键字参数允许你传入 0 个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个 dict 。
# **age 表示关键字参数（表示一个 dict ）。 age 只做表示，替代，不做展示。


def login(name, password, **other):
    print('name:', name, 'password:', password, 'other_age:', other)
    return name, password, other


any_param = login('张小霖', '123456', city='乐山')
print('传入任意参数后：', any_param)

# 关键字参数的复杂调用
dict_param = {'other_name': '蒙娜丽莎', 'age': 18, 'grade': '一班'}
complex_param = login('张小霖', '123456', **dict_param)
print('传入复杂参数后：', complex_param)

# 命名关键字参数（限制关键字参数）
# 作用：限制关键字参数的名字，就可以用命名关键字参数。
# 用法：和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# 注意：命名关键字参数必须传入定义的参数名。如果没有传入参数名，调用也将报错（必须传入定义的参数，多传少传都报错）；
# restrict_param('孙子', 45, '山东北部（齐国乐安）', '军事'))  # 由于没有传入定义的参数名，所以此行调用会报错。


def restrict_param(name, age, *, city, job):
    return name, age, city, job


# print('关键字参数为：', restrict_param('孙子', 45, city='山东北部（齐国乐安）')) # 会报错
# print('关键字参数为：', restrict_param('孙子', 45, city='山东北部（齐国乐安）', job='军事', wife='未知')) # 会报错
print('restrict_param 命名关键字参数：', restrict_param(
    '孙子', 45, city='山东北部（齐国乐安）', job='军事'))  # 正确

# 如果函数参数中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了；
# 这个可变参数仅作为后面参数的定义，不作为key值传递


def restrict_param_add(name, age, *, city, job):
    print(name, age, city, job)


restrict_param_add('带参数的 *args 含有 city ， job ：',
                   '年龄99', city='四川广元', job='我想成为一个军事家')
# print('restrict_param_add 中间含有命名关键字参数：', restrict_param_add(
#     '孙膑', '不详', city='山东省菏泽市甄城县北', job='军事'))

# 参数组合
# 在 Python 中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用，但是参数定义的顺序必须是：
# 必选参数、
# 默认参数、
# 可变参数、
# 命名关键字参数和关键字参数。


def compose_param1(a, b=0, *c, **d):
    print('组合参数1：a=', a, 'b=', b, 'c=', c, 'd=', d)


def compose_param2(a, b=0, *c, d, e, **f):
    print('组合参数2：a=', a, 'b=', b, 'c=', c, 'd=', d, 'e=', e, 'f=', f)


compose_param1('我是 compose_param1 的，必选参数a', '默认值b', [
               '可变参数list1', '可变参数list2'], param1='关键字参数1', param2='关键字参数2')
compose_param2('我是 compose_param2 的，必选参数a', '我是默认值b', [
               '可变参数c_list1', '可变参数c_list2'], d='命名关键字参数1', e='命名关键字参数2', f1="关键字f1", f2="关键字f2")

# 递归函数
# 函数在内部调用本身，这个函数就是递归函数。
# 所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
# 优点：逻辑简单清晰。
# 缺点：是过深的调用会导致栈溢出， Python 标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
# 注意：使用递归函数需要注意防止栈溢出。
# 知识：在计算机中，函数调用是通过栈（ stack ）这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧；
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
# n! = 1 x 2 x 3 x ... x n


def recursion(n):
    if n == 1:
        return 1
    return n * recursion(n - 1)


print('等差数列（从 5-1 ）的积为：', recursion(5))
# recursion(5) 的计算过程是：
# ===> fact(5)
# ===> 5 * fact(4)
# ===> 5 * (4 * fact(3))
# ===> 5 * (4 * (3 * fact(2)))
# ===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120
# print('测试栈溢出的情况：', recursion(1000))

# 尾递归函数
# 解决递归调用栈溢出的方法是通过尾递归优化，
# 事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
# 注意： recursion(n) 函数由于引入了 return n * fact(n - 1) 乘法表达式，所以不是尾递归；
# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的 recursion_last(n) 函数改成尾递归方式，也会导致栈溢出。


def recursion_last(n):
    return recursion_last_self(n, 1)


def recursion_last_self(num, product):
    if num == 1:
        return product
    print('我爱美女', num - 1, num * product)
    return recursion_last_self(num - 1, num * product)


recursion_last(5)
# print('尾递归函数 recursion_last(5) 计算结果为：', recursion_last(5))
# recursion(5) 的计算过程是：
# ===> fact_iter(5, 1)
# ===> fact_iter(4, 5)
# ===> fact_iter(3, 20)
# ===> fact_iter(2, 60)
# ===> fact_iter(1, 120)
# ===> 120
# print('尾递归函数 recursion_last(1000) 计算结果为：', recursion_last(1000))

# 递归实验汉诺塔的移动


def hanoi_tower(n, a, b, c):
    if n == 1:
        print('hanoi_tower', a, '-->', c)
    else:
        hanoi_tower(n-1, a, c, b)
        hanoi_tower(1, a, b, c)
        hanoi_tower(n-1, b, a, c)


hanoi_tower(4, 'A', 'B', 'C')
