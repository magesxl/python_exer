#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable

# 迭代操作
d = {'a': '2', 'b': '3'}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k + '  ' + v)

# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断

if isinstance(d, Iterable):
    for key in d:
        print(key)

# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身：


listA = [1, 6, 3, 2, 4]
if isinstance(listA, Iterable):
    for i, value in enumerate(listA):
        print(i, value)

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
listB = [1, 8, 6, 77, 3, 0]


def searchValue(listB):
    if isinstance(listB, Iterable):
        if listB == []:
            return None, None
        else:
            max_initial_value = listB[0]
            min_initial_value = listB[0]
            for v in listB:
                if v >= max_initial_value:
                    max_initial_value = v
                else:
                    min_initial_value = v
            return max_initial_value, min_initial_value;
    else:
        raise TypeError('传参有误')


print(searchValue(listB))
print(searchValue([]))
