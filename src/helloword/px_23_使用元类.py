# -*- coding:utf-8 -*-
__author__ = '朱永刚'

def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

h = Hello()
h.hello()

