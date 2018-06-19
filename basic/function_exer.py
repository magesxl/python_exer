#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def fun1(a):
    if isinstance(a, (int, float)):
        if a < 0:
            return abs(a)
        else:
            return a
    else:
        raise TypeError('传参有误')


print(fun1(11))


# 如果什么都不想做  可以定义一个空函数  可以防止代码运行语法错误
def fun_none():
    pass


def move_step(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move_step(100, 100, 60, math.pi / 6)
print(x, y)


# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
# 的两个解。
# 提示：计算平方根可以调用math.sqrt()函数：

def quadratic(a, b, c):
    params = [a,b,c,]
    for i in params:
        if not isinstance(i,int):
            raise TypeError('传参有误')

    delta = b * b - 4 * a * c
    if delta >= 0:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        print('两个参数解为\nx1=%.3f \nx2=%f' %(x1,x2))
        return x1,x2
    else:
        print('无解')

print(quadratic(2,5,2))
