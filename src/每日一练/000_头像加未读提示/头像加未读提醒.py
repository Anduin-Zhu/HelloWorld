# -*- coding:utf-8 -*-
__author__ = '朱永刚'
"""
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
"""
from PIL import Image, ImageDraw, ImageFont

# 打开图片文件
image = Image.open('0.png')
# 获取图片尺寸
w, h = image.size
# 规定字体类型及大小
font = ImageFont.truetype(font='arial', size=50)
# 创建一个可以绘图的对象
draw = ImageDraw.Draw(image)
# 在创建的对象上添加数字
draw.text((4 * w / 5, h / 5), '6', fill=(255, 10, 10), font=font)
# 保存图像
image.save('1.png', 'png')
