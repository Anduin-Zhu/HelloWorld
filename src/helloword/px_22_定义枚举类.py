# -*- coding:utf-8 -*-
__author__ = '朱永刚'

from enum import Enum

Mouth = Enum('Mouth',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))


for name,member in Mouth.__members__.items():
    print(name,'=>',member,',',member.value)



print((Mouth.Jan).value)

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

type()


