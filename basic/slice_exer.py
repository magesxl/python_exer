#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python提供了切片（Slice）操作符
list2 = [1, 2, 3, 4, 5]
print(range(4))


# 取前n个元素
def nYuansu(list, num):
    list1 = []
    for n in range(num):
        list1.append(list[n])
    return list1;


print(nYuansu(list2, 4))

print(list2[0:3])
print(list2[:3])
print(list2[1:3])

listA = list(range(50))
print(listA)
print(listA[::5])
print(listA[:20:5])
print(listA[:-10])
print(listA[-10:])
print(listA[:])

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
l = 'ABCDEF'
print(l[::2])

# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
oriStr = ' olikkk '

print(oriStr[1:-1])


def trim1(str):
    if len(str) == 0:
        return str
        while str[0] == '':
            str = str[1:]
        while str[-1] == '':
            str = str[0:-1]
        return str


def trim2(str):
    if len(str) == 0:
        return str
    elif str[0] ==' ':
        return trim2(str[1:])
    elif str[-1]==' ':
        return trim2(str[:-1])
    return str
print(trim2('  452  '))

l = '  452  '
print(l[0])
