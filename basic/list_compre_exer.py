#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 列表生成器
import os
print(list(range(1, 11)))


# 如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做
def num():
    l = []
    for i in range(1, 11):
        l.append(i * i)
    return l


print(num())

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print([x * x for x in range(2, 12)])

print([x * x for x in range(3, 13)
       if x % 2 == 0
       ])

#还可以使用两层循环，可以生成全排列：
print([x+y for x in 'abc' for y in '123'])

#运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
# os.listdir可以列出文件和目录
print([d for d in os.listdir('.')])
print([d for d in os.listdir('D:')])

#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
param_map = {'1':'张三','2':'李四'}
print([k+'='+v for k,v in param_map.items()])

#最后把一个list中所有的字符串变成小写：
param_list = ['HELLO','PLOUDJD','KJDHDH','GHRYH']
print([d.lower() for d in param_list])

#如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
#请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
def lower_param(param):
    pass



