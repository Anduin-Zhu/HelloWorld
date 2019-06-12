
'''
#定义一个行计数器
row = 1
#一个循环控制行号
while row <= 9:
    #定义列计数器
    col = 1
    while col <= row:
        print("%s * %s = %s"%(col,row,row * col),end="\t")
        col += 1
    print("")
    row += 1'''

row = 1
while row <= 9:
    #设置一个计数器
    col = 1
    #while条件
    while col <= row:

        print("%s * %s = %s" %(col,row,col * row),end="\t")
        col += 1
    print("")
    row += 1
