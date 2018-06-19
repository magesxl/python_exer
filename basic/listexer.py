#!/usr/bin/env python3
# -*- coding: utf-8 -*-
list1=['11','2','3']
print(len(list1))
print(list1[0])
print(list1[len(list1)-1])
print(list1)
#末尾追加元素
list1.append('你好')
#指定索引
list1.insert(1,'你好1')
print(list1)
#list1.pop()
#list1.pop(1)
list2=[1,'你好']
list1.append(list2)
print(list1)

#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
tuple1 = (1,2,3)
tuple2 = (2,)
print(tuple2)
print(len(tuple1))
for name in list1:
    print(name)

for name in tuple1:
    print(name)
#python  集合  list  tuple


