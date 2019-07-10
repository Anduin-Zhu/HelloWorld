# -*- coding:utf-8 -*-
__author__ = '朱永刚'

def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def foo2(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

import logging
logging.basicConfig(level=logging.INFO)

def foo3(s):
    n = int(s)
    logging.info('n = %d' % n)
    return 10 / n

def main():
    foo3('0')

main()