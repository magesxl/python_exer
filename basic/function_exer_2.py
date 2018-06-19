#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
def muliData(x):
    return x*x
print(muliData(2))


def muliNData(num,n=2):
    total = 1
    i = 0
    while(i<n):
        total = total*num
        i = i+1
    return total
print(muliNData(3,2))

# 计算 a^2+b^2+c^2+...  还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
# 可以把a，b，c……作为一个list或tuple传进来
def deDeta(numbers):
    total = 0;
    for n in numbers:
        total = total+n*n

    return  total

print(deDeta([1,2,2]))
print(deDeta((1,2,2)))
print(deDeta((1,)))

def deDate1(*numbers):
    total = 0
    for n in numbers:
        total = total+math.pow(n,2)
    return total
print(deDate1(2,))
print(deDate1())
print(deDate1(1,2,2))
num = [1,2,3]
#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见
print(int(deDate1(*num)))

#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
    if 'wo' in kw:
        pass
        print('姓名：%s 年龄：%s 其他：%s' %(name,age,kw))

print(person('1',3))
print(person('2',5,name1='nihao'))


#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
extra = {'wo':1,'bihao':2}
print(person(1,2,**extra))

#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name,age,*,city,job):
        print(name,age,city,job)
print(person(1,2,city=3,job=5))

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, city, job)


def chengji(*num):
    total = 1;
    for i in num:
        total = total*i
    return total
print(chengji(1,2,3))




