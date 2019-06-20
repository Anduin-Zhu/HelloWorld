# -*- coding:utf-8 -*-
__author__ = '朱永刚'


class A(object):
    __slots__ = ('name','age')

class B(A):
    pass

a = A()

a.name = 2

