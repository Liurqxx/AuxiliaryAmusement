# _*_coding:utf-8_*_
# Author:liu
import requests
import re
from tkinter import *
from tkinter import messagebox


# 模拟浏览器发送请求
def download():
    startUrl = 'http://www.uustv.com/'
    # 接收用户输入的名字
    name = entry.get()

    # 对用户输入的名字进行处理
    name = name.strip()

    if name == '':
        # 弹窗提示
        messagebox.showinfo('提示：', '请输入用户名')
    else:
        data = {
            'word': name,
            'sizes': 60,
            'fonts': 'jfcs.ttf',
            'fontcolor': '# 000000',
        }
        # 获取网站源代码
        result = requests.post(startUrl, data=data)
        result.encoding = 'utf-8'
        html = result.text
        # print(html)
        # 正则
        reg = '<div class="tu">.*?<img src="(.*?)"/></div>'
        # 图片路径
        imagePath = re.findall(reg, html)
        # 图片完整的路径
        imgUrl = startUrl + imagePath[0]
        # 获取图片信息
        response = requests.get(imgUrl).content

        # print(imgUrl)

        # 保存图片
        with open('{}.gif'.format(name), 'wb') as file:
            file.write(response)

        # 显示图片
        bm = PhotoImage(file='{}.gif'.format(name))

        label2 = Label(root, image=bm)
        label2.bm = bm
        label2.grid(row=2, columnspan=2)



