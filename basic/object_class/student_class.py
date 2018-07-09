#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，
这个对象拥有name和score这两个属性（Property）。如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，
给对象发一个print_score消息，让对象自己把自己的数据打印出来。
'''

"""
__init__ 方法的主要作用,就是初始化你的属性
注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
"""

"""
和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数
"""
class Student(object):
    #__init__ 方法的主要作用,就是初始化你的属性
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print(self.score)


stu1 = Student("xiaoli",89)
stu1.print_score()

