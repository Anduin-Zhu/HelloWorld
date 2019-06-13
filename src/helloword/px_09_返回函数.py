# -*- coding:utf-8 -*-
__author__ = '朱永刚'


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


"""
利用闭包返回一个计数器函数，每次调用它返回递增整数：
"""


def createCounter():
    i = 0

    def counter():
        nonlocal i
        i += 1
        return i

    return counter


if __name__ == '__main__':
    f1 = lazy_sum(1, 3, 5, 7, 9)
    print(f1())
    x = createCounter()
    print(x(), x(), x())
