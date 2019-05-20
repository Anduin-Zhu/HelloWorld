# -*- coding:utf-8 -*-
__author__ = '朱永刚'
"""
名片管理系统
 1. 程序启动，显示名片管理系统欢迎界面，并显示功能菜单
**************************************************
欢迎使用【名片管理系统】V1.0
1. 新建名片
2. 显示全部
3. 查询名片
0. 退出系统
**************************************************
* 2. 用户用数字选择不同的功能
* 3. 根据功能选择，执行不同的功能
* 4. 用户名片需要记录用户的 **姓名**、**电话**、**QQ**、**邮件**
* 5. 如果查询到指定的名片，用户可以选择 **修改** 或者 **删除** 名片
"""

#定义一个空列表来存储名片
card_list = []
#启动程序打印主界面
while 1:
    print(("*" * 30 +
           "\n欢迎使用【名片管理系统】V1.0\n"
           "1. 新建名片\n"
           "2. 显示全部\n"
           "3. 查询名片\n"
           "0. 退出系统\n"
           + "*" * 30))
    #获取用户输入,让用户选择功能
    user_input = input()
    #如果选择1，就新建名片
    if user_input == "1":
        #增加一个循环可以重复添加名片
        while 1:
            name_input = input("请输入你的姓名：")
            tel_input = input("请输入你的电话号码：")
            qq_input = input("请输入你的QQ：")
            mail_input = input("请输入你的邮件：")
            card = {"姓名":name_input,"电话":tel_input,"QQ":qq_input,"邮箱":mail_input}
            card_list.append(card)
            #判断是否继续添加名片
            if input("请问是否继续添加名片？\n1.继续添加\n2.按任意键返回主菜单\n") == "1":
                continue
            else:
                break
    #如果选择2，就显示全部名片
    elif user_input == "2":
        for card in card_list:
            print("姓名：%s\n"
                  "电话：%s\n"
                  "QQ:%s\n"
                  "邮箱：%s\n"%(card["姓名"],card["电话"],card["QQ"],card["邮箱"]))

    #如果选择3，就进入名片查询界面
    elif user_input == "3":
        name_chaxun = input("请输入要查询姓名：")
        for card in card_list:
            if card["姓名"] == name_chaxun:
                print("姓名：%s\n"
                      "电话：%s\n"
                      "QQ:%s\n"
                      "邮箱：%s\n" % (card["姓名"], card["电话"], card["QQ"], card["邮箱"]))
                #查询到的名片可以进行修改或者删除
                name_caozuo = input("请选择要进行的操作：\n1. 修改名片\n2. 删除名片\n3. 按任意键回到主菜单\n")
                if name_caozuo == "1":
                    card["电话"] = input("请输入你的电话：")
                    card["QQ"] = input("请输入你的QQ：")
                    card["邮箱"] = input("请输入你的邮箱地址：")
                elif name_caozuo == "2":
                    card_list.remove(card)
                else:
                    break
                break
        else:
            print("抱歉，没有找到姓名为%s的人" % card["姓名"])

    #如果选择0，就退出系统
    elif user_input == "0":
        break
    #如果输入其他就提示输入错误，重新输入
    else:
        print("输入错误，请重输入！！！")