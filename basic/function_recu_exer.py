#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#据算1+2+3+4+5+6+...
def recu(n):
    if n==1:
        return 1
    else:
        return recu(n-1)+n

print(recu(2))

#在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出
#解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，
# 使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

def recu1(n):
        return recu(n,1)
def recu(n,product):
    if n==1:
        return product
    else:
        return recu(n-1,n+product)
print(recu1(5))

