#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import  reduce
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回


#比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下

list1=list(range(1,10))
print(list1)


def xt_num(x):
    return x*x

l = map(xt_num,list1)
print(list(l))

print(list(map(str,list1)))


#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#比方说对一个序列求和，就可以用reduce实现：

def add(x,y):
    return x+y
print(reduce(add,list1))

#要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场
def add1(x,y):
    return x*10+y
print(reduce(add1,list1))


#如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(str1):
    def f1(x,y):
        return 10*x+y
    def f2(str1):
        return DIGITS[str1]
    return reduce(f1,map(f2,str1))
print(str2int('789'))

#用lambda函数进一步简化成
def f3(str2):
    return DIGITS[str2]
def str2intl(str1):
    return reduce(lambda x,y:10*x+y,map(f3,str1))
print(str2intl('7895'))
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
list3 =['adam', 'LISA', 'barT']
def format1(str1):
        s = str1[0].upper()+str1[1:].lower()
        return s
print(list(map(format1,list3)))

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(x,y):
    return x*y
print(reduce(prod,list1))

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(str3):
    s1 = str3.split('.')[0]
    s2 = str3.split('.')[1]


