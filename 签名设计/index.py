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

# 定义点击按钮 command:触发事件
button = Button(root, text='设计签名', font=('微软雅黑', 20), command=download)
# 定位
button.grid(row=1, column=0)

# 消息循环
root.mainloop()
