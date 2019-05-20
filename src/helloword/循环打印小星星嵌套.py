"""
打印五行小星星，每行小星星与行数一致
"""

row = 1
while row <= 5:
    #设置一个计数器
    col = 1
    #while条件
    while col <= row:

        print("*",end="")

        col += 1
    print("")
    row += 1
'''

row = 1

while row <= 5:
    col = 1
    while col <= row:
        print("*" )

    row += 1'''