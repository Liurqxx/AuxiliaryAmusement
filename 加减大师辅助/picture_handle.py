# _*_ coding:utf-8 _*_
# Author:liu
from PIL import Image
from pytesseract import *

# 上面都是导包，只需要下面这一行就能实现图片文字识别
# text = pytesseract.image_to_string(Image.open('2.png'), lang='chi_sim')  # 设置为中文文字的识别
# text = pytesseract.image_to_string(Image.open('2.png'), lang='eng')  # 设置为英文或阿拉伯字母的识别
# print(text)
from PIL import Image
import numpy as np


import sys

# 二值化
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

# 由于都是数字
# 对于识别成字母的 采用该表进行修正
rep = {'O': '0',
       'I': '1', 'L': '1',
       'Z': '2',
       'S': '8',
       };


def getverify1(name):
    # 打开图片
    im = Image.open(name)
    # 转化到灰度图
    imgry = im.convert('L')
    print(imgry)
    # 保存图像
    imgry.save('g' + name)
    # 二值化，采用阈值分割法，threshold为分割点
    out = imgry.point(table, '1')
    print(out)
    out.save('b' + name)
    # 识别
    text = image_to_string(out)
    print('text==', text)
    # 识别对吗
    text = text.strip()
    text = text.upper();
    for r in rep:
        text = text.replace(r, rep[r])
        # out.save(text+'.jpg')
    print(text)

    return text


getverify1('2.png')
