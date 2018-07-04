#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable


# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。
# 在一个list中，删掉偶数，只保留奇数，可以这么写：
def filter_list(n):
    return n % 2 == 0


print(list(filter(filter_list, [1, 2, 3, 4, 5, 6])))


def not_empty(n):
    return n and n.strip()


print(list(filter(not_empty, ['A', '2', '', 'B', None, 'C', '  '])))

print(' abv'.strip())


# 计算素数的一个方法
# 可以先构造一个从3开始的奇数序列：  这是一个生成器，并且是一个无限序列。
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 定义一个筛选函数：
def _not_divisible(n):
    return lambda x: x % n > 0


# 定义一个生成器，不断返回下一个素数：  这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


# 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：

# 打印10以内的素数:
for n in primes():
    if n < 10:
        print(n)
    else:
        break

a = 'abcops'
print(a[::-1])


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def number_of_times_filter(s):
    s = str(s)
    return s == s[::-1]
print(list(filter(number_of_times_filter,range(1,200))))


