# -*- coding:utf-8 -*-
__author__ = '朱永刚'


def bulid(x, y):
    return lambda: x ** 2 + y ** 2


def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print(L)

l2 = list(filter(lambda x: x % 2 == 1, range(1, 20)))
