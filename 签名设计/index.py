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
if __name__ == '__main__':
    # 创建窗口
    root = Tk()
    # 标题
    root.title('签名设计')
    # 设置窗口大小 宽x高
    root.geometry('600x300')
    # 窗口初始位置
    root.geometry('+500+200')

    # 设置标签 root:所在窗口
    label = Label(root, text='签名', font=('华文行楷', 20), fg='red')
    # 定位方式:grid pack place
    # 显示在第0行第0列
    label.grid()  # 等价于：label.grid(row=0, column=0)

    # 输入框
    entry = Entry(root, font=('微软雅黑', 20))
    # 显示在第0行第1列
    entry.grid(row=0, column=1)
    # 程序运行时光标停在此处
    entry.focus()

    # 定义点击按钮 command:触发事件
    button = Button(root, text='设计签名', font=('微软雅黑', 20), command=download)
    # 定位
    button.grid(row=1, column=0)

    # 下拉菜单
    # 创建一个下拉列表
    font_list = StringVar()
    # state:把菜单设置为只读模式
    fontChosen = ttk.Combobox(root, width=12, textvariable=font_list, font=('微软雅黑', 20), state='readonly')

    # 设置下拉列表的值
    fontChosen['values'] = ('个性签', '连笔签', '潇洒签', '草体签', '合文签', '商务签', '可爱签')
    # 设置其在界面中出现的位置  column代表列   row 代表行
    fontChosen.grid(column=1, row=1)
    # 设置下拉列表默认显示的值，0为 fontChosen['values'] 的下标值
    fontChosen.current(0)

    # 消息循环
    root.mainloop()
    print('程序退出')