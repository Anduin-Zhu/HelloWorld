# -*- coding:utf-8 -*-
__author__ = '朱永刚'
'''
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
'''


def sum_numbers(*args):
    sum = 0
    for temp in args:
        sum += temp
    return sum, temp


print(type(sum_numbers(1, 2, 3)))
print(sum_numbers(1, 3, 4, 5))

'''
def demo(num, num_list):
	print("函数内部")
	# 赋值语句
	num = 200
	num_list = [1, 2, 3]
	print(num)
	print(num_list)
	print("函数代码完成")

glnum = 99
gllist = [4, 5, 6]
demo(glnum, gllist)

print(glnum)#200
print(gllist)#[1,2,3]
'''
'''
def demo(num, num_list):
	print("函数内部代码")
	num += num
	# num_list.extend(num_list) 由于是调用方法，所以不会修改变量的引用
	# 函数执行结束后，外部数据同样会发生变化
	num_list += num_list
	print(num)
	print(num_list)
	print("函数代码完成")
glnum = 9
gllist = [1, 2, 3]
demo(glnum, gllist)
print(glnum)
print(gllist)'''


def jiaohuan(a, b):
    a, b = b, a
    print(a, b)


a = 1
b = 2
jiaohuan(a, b)
