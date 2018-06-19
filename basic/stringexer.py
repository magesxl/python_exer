#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(ord("A"))
print(chr(66))
print(0xff)
charset = "utf-8"
x = '男孩'
encodex = x.encode(charset)
print(x.encode(charset))
x = encodex.decode(charset, errors='ignor')
print(x)
print(len(x))
print(len(encodex))
abc = 'woshi:20+30=%s' % (20 + 30)
print(abc)
print('woshi:20+30=%d' % (20 + 30))

print('age:%s,xingming:"%s"' % (89, '世博'))

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

s1 = 71
s2 = 89
s3 = (s2 - s1) / s1
print('小明成绩提升了%.3f%%' % s3)

ccbPublicKey = "30819c300d06092a864886f70d010101050003818a0030818602818071f611ae71f7c135a03972abfcb2cacb480eea1e3e6da23e58e109fd35251e182b25633ccb341b524e745e9e13f50bac905de2d1a3a44a2adc3346f8dac7c6ff85eb15d238317d76d66a1d2736cbc3a4546a46b6a61c09e24a12815e5fd63021322dfa62cf3b139395a300ee0168a5a2d91c072158cd52345503510928948d11020111";
