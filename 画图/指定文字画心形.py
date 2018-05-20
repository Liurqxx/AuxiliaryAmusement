# _*_ coding:utf-8 _*_
# Author:liu

import time

words = input('Please input the words you want to say!:')
# 例子：words = "Dear lili, Happy Valentine's Day! Lyon Will Always Love You Till The End! ♥ Forever!  ♥"
for item in words.split():
    # 要想实现打印出字符间的空格效果，此处添加：item = item+' '
    letterlist = []  # letterlist是所有打印字符的总list，里面包含y条子列表list_X

