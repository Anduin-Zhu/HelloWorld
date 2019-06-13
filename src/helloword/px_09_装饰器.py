# -*- coding:utf-8 -*-
__author__ = '朱永刚'


# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
    print('2019-06-13')


# 函数对象有一个__name__属性，可以拿到函数的名字：
print(now.__name__)


# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# decorator就是一个返回函数的高阶函数。

def log(func):
    def wapper(*args, **kwargs):
        print('call%s()' % func.__name__)
        return func(*args, **kwargs)

    return wapper


@log
def now2():
    print('2019-06-13')


now2()
print(now2.__name__)

"""
请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
"""
import time, functools


# print(time.strftime('%Y.%m.%d %H:%M:%S ',time.localtime(time.time())))

def metric(func):
    @functools.wraps(func)
    def return_time(*args, **kwargs):
        print('%s executed in %s s' % (func.__name__, time.strftime
        ('%Y.%m.%d %H:%M:%S ', time.localtime(time.time()))))
        return func(*args, **kwargs)

    return return_time


@metric
def add(x, y):
    print(x + y)


# add(1,2)
from functools import wraps


def log(note=None):
    '''一个log的decorator，它既支持@log(),
        又支持：@log('execute')
    '''
    text = str(note) if note else ''

    # 相当于
    # if note:
    #     text3 = str(note)
    # else:
    #     text3 = ''
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'begin call {func.__name__}')
            res = func(*args, **kwargs)
            print(f'end call {func.__name__}, {text} finish.')
            return res

        return wrapper

    return decorator


@log()
def f1():
    print('running in f1().')


@log('execute')
def f2():
    print('running in f2().')


if __name__ == '__main__':
    f1()
    print('**' * 15)
    f2()
