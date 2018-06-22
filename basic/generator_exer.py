#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#生成器  在Python中，这种一边循环一边计算的机制，称为生成器：generator。
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
#创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
print((x*x for x in range(10)))




