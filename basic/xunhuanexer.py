#!/usr/bin/env python3
# -*- coding: utf-8 -*-
list1 = list(range(101))
sum = 0
for i in list1:
    sum = sum + i
print(sum)

sum1 = 0
number = 99
while number > 0:
    sum1 = sum1 + number
    number = number - 2
print(sum1)

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
