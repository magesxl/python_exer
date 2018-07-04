#!usr/bin/env python3
# -*- coding: utf-8 -*-
# 内置的sorted()函数就可以对list进行排序
list1 = [-2, 9, 5, 6, -3]
print(sorted(list1))
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
print(sorted(list1, key=abs))


list_str = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(list_str,key=str.lower,reverse=True))

#假设我们用一组tuple表示学生名字和成绩：请用sorted()对上述列表分别按名字排序： 再按成绩从高到低排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
map = ('Bob', 75)
print(map[0])
print(sorted(L,key=lambda i:i[0]))
print(sorted(L,key=lambda i:i[1],reverse=True))
def by_name(t):
    return t[0]