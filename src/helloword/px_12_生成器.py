# -*- coding:utf-8 -*-
__author__ = '朱永刚'

"""
杨辉三角
"""


def yangHui(max):
    l = [1]
    i = 0
    while i < max:
        yield l
        l = [1] + [l[temp] + l[temp + 1] for temp in range(len(l) - 1)] + [1]
        i += 1

y = yangHui(10)
print(next(y))
print(next(y))
print(next(y))



# for i in yangHui(10):
#     print(i)

l4 = [1,3,3,1]
#l5 = [1,4,6,4,1] # l5 = [1,l4[0] + l4[1],l4[1] + l4[2],l4[2] + l4 [3],1]
l5 = [1,l4[0] + l4[1],l4[1] + l4[2],l4[2] + l4 [3],1]
a = iter("abcder")

