# _*_coding:utf-8_*_
# Author:liu
import re
import requests
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# 获取字体
def getFont(name):
    font_list_name = {
        '个性签': 'jfcs.ttf',
        '连笔签': 'qmt.ttf',
        '潇洒签': 'bzcs.ttf',
        '草体签': 'lfc.ttf',
        '合文签': 'haku.ttf',
        '商务签': 'zql.ttf',
        '可爱签': 'yqk.ttf',
    }
    return font_list_name[name]

# 模拟浏览器发送请求
def download():
    # 请求url地址
    startUrl = 'http://www.uustv.com/'

    # 接收用户输入的名字
    name = entry.get()

    # 对用户输入的名字进行处理
    name = name.strip()

    # 获取用户选择的字体
    select_font = fontChosen.get()

    if name == '':
        # 弹窗提示
        messagebox.showinfo('提示：', '请输入用户名!')


    else:
        data = {
            'word': name,
            'sizes': 60,
            'fonts': getFont(select_font),
            'fontcolor': '# 000000',
        }

        # 获取网站源代码
        result = requests.post(startUrl, data=data)
        result.encoding = 'utf-8'
        html = result.text
        # print(html)
        # 正则匹配图片路径
        reg = r'<div class="tu">.*?<img src="(.*?)"/></div>'
        # 图片路径
        imagePath = re.findall(reg, html)
        # 图片完整的路径
        imgUrl = startUrl + imagePath[0]
        # 获取图片信息
        response = requests.get(imgUrl).content

        # 保存图片
        with open('{}.gif'.format(name), 'wb') as file:
            file.write(response)

        # 显示图片
        bm = PhotoImage(file='{}.gif'.format(name))
        # 把图片显示到窗口上
        label2 = Label(root, image=bm)
        label2.bm = bm
        label2.grid(row=2, columnspan=2)
