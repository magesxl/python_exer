#!/usr/bin/env python3
# -*- coding: utf-8 -*-
f = open('D://上线准备.txt','r')
print(f.read())
f.close()


with open('D://上线准备.txt','r') as f:
    for line in f.read():
        print(line.strip())
