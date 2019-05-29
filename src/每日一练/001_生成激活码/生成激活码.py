# -*- coding:utf-8 -*-
__author__ = '朱永刚'
"""
做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
"""

import uuid,re

def create_num(num,length=16):

    result = []
    while num > 0:
        uuid_id = uuid.uuid1()
        temp = str(uuid_id).replace('-','')[:length]
        temp2 = '-'.join(re.compile('.{4}').findall(temp))
        if temp2 not in result:
            result.append(temp2)
            num -= 1
    return result

if __name__ == '__main__':
    print(uuid.uuid1())
    print(create_num(200))