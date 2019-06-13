# -*- coding:utf-8 -*-
__author__ = '朱永刚'


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7])

"将字符串的第一个字符转为大写".capitalize()
"转换字符串中所有大写字符为小写.".lower()
"转换字符串中的小写字母为大写".upper()
"返回'标题化'的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())".title()
"将字符串中大写转换为小写，小写转换为大写".swapcase()

"""
利用map()函数，把用户输入的不规范的英文名字，
变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，
输出：['Adam', 'Lisa', 'Bart']
"""


def normalize(name):
    return name.title()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

"""
Python提供的sum()函数可以接受一个list并求和，
请编写一个prod()函数，可以接受一个list并利用reduce()求积：
"""
from functools import reduce


def prod(list):
    def fun(x, y):
        return x * y

    return reduce(fun, list)


print(prod([3, 5, 7, 9]))

"""
利用map和reduce编写一个str2float函数，
把字符串'123.456'转换成浮点数123.456
"""


def str2float(s):
    def fun(x, y):
        return x * 10 + y

    l1, l2 = s.split('.')
    return reduce(fun, map(float, l1)) + reduce(fun, map(float, l2)) / (10 ** len(l2))


print(str2float("123.456"))


def is_odd(n):
    return n % 2 == 1


list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))

"""
埃氏筛法求素数
"""


# 构造一个生成器，生成以三开始的所有奇数
def odd_iter():
    """
    返回以三开始的所有奇数
    :return:
    """
    i = 1
    while 1:
        i += 2
        yield i


# 筛选器，
def not_divisible(n):
    return lambda x: x % n > 0


# 素数生成器
def primes():
    yield 2
    li = odd_iter()
    while 1:
        n = next(li)
        yield n
        li = filter(not_divisible, li)


'''
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
    '''


# 生成器，全体自然数

def natural():
    i = 1
    while 1:
        i += 1
        yield i


# 筛选器，
def not_huishu(n):
    if str(n) == str(n)[::-1]:
        return True


def huishu():
    li = natural()
    while 1:
        n = next(li)
        yield n
        li = filter(not_huishu, li)


'''
for n in huishu():
    if n < 100:
        print(n)
    else:
        break'''

"""
分别按照名字和成绩排序。
"""
L222 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    L333 = []
    name_dict = {}
    for i in dict(t).keys():
        L333.append(i)
    name_list = sorted(L333)
    for i in name_list:
        name_dict[i] = dict(t)[i]
    return [(key, value) for key, value in zip(name_dict.keys(), name_dict.values())]


def by_name2(t):
    return t[0]


def by_score(t):
    return t[1]


print(sorted(L222, key=by_name2))
print(sorted(L222, key=by_score))
