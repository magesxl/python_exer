#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(abs(-10))
print(abs)
# abs(-10)是函数调用，而abs是函数本身。
# 要获得函数调用结果，我们可以把结果赋值给变量：
#结论：函数本身也可以赋值给变量，即：变量可以指向函数。
f = abs
print(f(-15))
#当运行 abs = 10 以后，如果想恢复 abs 函数，只要运行 del abs 就可以了。
#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x,y,f):
    return f(x)+f(y)

print(add(-1,-2,abs))