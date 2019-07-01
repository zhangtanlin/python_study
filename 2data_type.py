#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 整数
print('十进制整数：', 1, 100, -8080, 0, '十六进制整数：', 0xff00, 0xa5b4c3d2)

# 浮点数
print('浮点数：', 1.23e9, -9.01, 1.23, -1.23e9)

# 字符串
print('字符串', 'abcdef', "aaaa'bbbb'cccc", 'aaaa"bbbb"cccc')

# 转译
print('转译', '我爱的人是\'孙子、孔子\'')
print(r'\\\\\\\\\\\\\\全\\\部\\\转\\\\\译\\\\\\')
print('换行\n换行')
print(r'''三个引号是什么意思？,\n即使加了转译，我有全局转译所以不换行''')

# 布尔值
print('否：', False, '不能写成false。', 0 > 50)
print(False and 0 < 50, False or True, not True)
if False or True:
    print('if成功')
else:
    print('if失败')

# 空值
print('空值用None表示，不能理解为0，0是有意义的，None是特殊的空值', None)

# 变量
number1 = 123456789
number2 = number1
number1 = 987654321
print('变量nunber1:', number1, '变量nunber2:', number2)

# 常量
# 全部大写表示常量是习惯用法，如果一定要常亮的值，也没人能拦住
NUMBER3 = '我是一个常量'
print(NUMBER3)

# byte
string1 = b'ABC'
print(string1, 'string1的数据类型是：', type(string1))

#编码转换
# Unicode表示的str通过encode()方法可以编码为指定的bytes(字节流)
string2 = 'ABCD'
string3 = '中文'
print('string2字符串类型转为ASSIC(字节流):', string2.encode('ascii'))
print('string3中文字符串类型转为utf-8(字节流):', string3.encode('utf-8'))
string4 = b'abcd'
string5 = b'\xe4\xb8\xad\xe6\x96\x87'
print('string4的bytes(字节流)数据类型转换为字符串:', string4.decode('ascii'))
print('string5的bytes(字节流)数据类型转换为字符串:', string5.decode('utf-8'))
string6 = b'\xe4\xb8\xad\xff'
# print('字节流包含无法解码的会报错：', string6.decode('utf-8'))
print('字节流包含无法解码的会报错，但是可以忽略错误的字节：', string6.decode('utf-8', errors='ignore'))
