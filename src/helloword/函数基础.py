# -*- coding:utf-8 -*-
__author__ = '朱永刚'

num = 0

def sun_numbers(*args):
    for temp in args:
        global num
        num += temp

    return num

print(sun_numbers(1,2,3,4,6,5))

def person(bixu,*args,moren = '默认',mmgjz,**kwargs):
    print(bixu,moren,args,mmgjz,kwargs)

person('必须',1,2,3,moren='moren',mmgjz='命名关键字',a=1,b=2,c=3)
