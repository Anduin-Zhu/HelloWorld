def demo(num, num_list):
    print("函数内部")
    num = 100
    num_list = [1, 2, 3]
    print(num)
    print(num_list)
    print("代码完成")


glnum = 200
glnum_list = [4, 5, 6]


# demo(glnum,glnum_list)
# print(glnum)
# print(glnum_list)

def demo2(num_list):
    num_list.extend([1, 2, 3])
    print(num_list)


# demo2(glnum_list)
# print(glnum_list)

def demo3(num, num_list):
    print("开始")
    num += num
    num_list += num_list  # 列表+=的本质是在调用extend方法
    print(num)
    print(num_list)
    print("完成")


demo3(glnum, glnum_list)
print(glnum)
print(glnum_list)
