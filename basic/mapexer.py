#!/usr/bin/env python3
# -*- coding: utf-8 -*-
name = {"name":111,"illk":89}
print(name.get('name'))

if 'ba' in name:
    print('a')
else:
    print('b')


print(name.get('b'))
#删除
name.pop('name')
print(name)

# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
#
# 和list比较，dict有以下几个特点：
#
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
#set集合
setname = set(['1',2,2,3])
print(setname)