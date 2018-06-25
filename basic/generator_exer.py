#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#生成器  在Python中，这种一边循环一边计算的机制，称为生成器：generator。
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
#创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
print((x*x for x in range(10)))
g = (x*x for x in range(10))
print(next(g))

def g_exer(g):
    for x in g:
        print(x)

print(g_exer(g))

# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易
def fibonacci(max):
    n,a,b=0,0,1
    while n<=max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'DONE'

print(fibonacci(5))
# fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
# 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
def g_fibonacci(max):
    n,a,b=0,0,1
    while n<=max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'END'

print(g_fibonacci(5))

#最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def old():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3
g_1=old()
print(next(g_1))
print(next(g_1))

#用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
def g_fun():
    g_2 = g_fibonacci(6)
    while True:
        try:
            x = next(g_2)
            print('值：',x)
        except StopIteration as e:
            print('返回值为：',e.value)
            break
print(g_fun())
def yhsj(num):
    g_yh = [1]                                   # 杨辉三角第一行
    MAX = 256                                 # 最大行数
    if num>=MAX:
        num = MAX
    for n in range(num):
        yield g_yh
        # 从第二行开始，除去两边的1，用一个列表生成器生成中间的列表
        g_yh = [1] + [g_yh[i]+g_yh[i+1] for i in range(n)] + [1]


result = []
for t in yhsj(6):
    print(t)
    result.append(t)

